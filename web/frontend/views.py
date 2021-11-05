import json, time, os

from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, resolve_url
from django.conf import settings
from celery.result import AsyncResult
from celery.execute import send_task
from celery import current_app 

from web.utils import reverse
from . import forms
from scripts import models as scripts
from storage import tasks as storage
from monitor import tasks as monitor

API_URL = settings.EXTERNAL_API_URL

DEFAULT_ARGS = {
        'api_url': API_URL
    }

def index(request):
    return render(request, 'home.html')

def refresh(request):
    result = monitor.build_network_graph.delay()
    result.get() #Todo: Logging proxy has no attribute encoding???
    image_path = os.path.join(settings.BASE_DIR, "static/docker-graph.svg")
    with open(image_path, 'w') as f:
        f.write(result.result)
    return HttpResponseRedirect(reverse('frontend:index'))

def about(request):
    return render(request, 'about.html')

def docs(request):
    docs = scripts.Doc.objects.all()
    return render(request, 'docs.html', {'result': docs})

def doc_view(request, doc_id):
    doc = scripts.Doc.objects.get(pk=doc_id)
    form = forms.DocForm(instance=doc)

    if request.method == 'POST':
        form = forms.DocForm(request.POST, instance=doc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    
    return render(request, 'create_doc.html', {'form': form})

def peers(request):
    peers = scripts.Peer.objects.all()
    return render(request, 'peers.html', {'result': peers})

def peer_view(request, peer_id):
    peer = scripts.Peer.objects.get(pk=peer_id)
    form = forms.PeerForm(instance=peer)

    if request.method == 'POST':
        form = forms.PeerForm(request.POST, instance=peer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    
    return render(request, 'create_peer.html', {'form': form})

def peer_create(request):
    form = forms.PeerForm()

    if request.method == 'POST':
        form = forms.PeerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, 'create_peer.html', {'form': form})

def doc_create(request):
    form = forms.DocForm()

    if request.method == 'POST':
        form = forms.DocForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('frontend:docs'))
        else:
            return HttpResponseBadRequest()

    return render(request, 'create_doc.html', {'form': form})

def files(request):
    form = forms.FileForm()
    if request.method == 'POST':
        form = forms.FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            storage.put_content.delay(data['content'], data['filename'])
            return HttpResponseRedirect(reverse('frontend:files'))
    args = {
        'api_url': API_URL
    }
    return render(request, 'files.html', {'args': DEFAULT_ARGS, 'form': form})

def create_file(request):
    form = forms.FileForm()
    if request.method == 'POST':
        form = forms.FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            storage.put_content.delay(data['content'], data['filename'])
            return HttpResponseRedirect(reverse('frontend:files'))
    return render(request, 'create_file.html', {'form': form})

def list_files(request):
    task = storage.list_files.delay()
    task.get()
    result = task._get_task_meta()
    files = result.get('result').get('files')
    return render(request, 'files_list.html', {'args': DEFAULT_ARGS, 'result': files})

def view_file(request, filename):
    task = storage.get_content.delay(filename)
    task.get()
    result = task._get_task_meta()
    file = result.get('result')
    if request.method == 'POST':
        form = forms.FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            storage.put_content.delay(data['content'], data['filename'])
            return HttpResponseRedirect(reverse('frontend:files'))
    form = forms.FileViewForm(file)
    return render(request, 'create_file.html', {'form': form})
        

def prepare_task(request):
    form = forms.TaskForm()
    return render(request, 'start_task.html', {'form': form, 'API_URL': API_URL})
    
def show_task_result(request, task_id):
    async_result = AsyncResult(task_id)
    async_result.get()
    result = async_result._get_task_meta()

    data = []
    if isinstance(result.get("result"), dict):
        if result.get('result').get('children'):
            for child in result.get('result')['children']:
                child_async = AsyncResult(child['task_id'])
                child_result = child_async._get_task_meta()
                data.append({
                    'task_id': child.get('task_id'),
                    'name': child_async.name,
                    'args': str(child_async.args),
                    'kwargs': str(child_result.get('kwargs')),
                    'status': child_result.get('status'),
                    'worker': child_result.get('worker'),
                    'date_done': child_result.get('date_done')
                })
            return render(request, 'task_children_list.html', {'children': data, 'origin': task_id})
    
    data = str(result.get('result')).replace("\\n\\r", "\n\r"), # remove escape characters

    form = forms.TaskResultForm({"result": data}) 
    return render(request, 'task_result.html', {'form': form})
