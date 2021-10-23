from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from web.utils import reverse
from . import forms
from scripts import models as scripts
from storage import tasks as storage

def index(request):
    return render(request, 'base.html')

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
    
    return render(request, 'base_view.html', {'form': form})

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
    
    return render(request, 'base_view.html', {'form': form})

def files(request):
    args = {
        'api_url': settings.API_URL
    }
    return render(request, 'files.html', {'args': args})

def create_file(request):
    form = forms.FileForm()
    if request.method == 'POST':
        form = forms.FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            storage.put_content.delay(data['filename'], data['content'])
            return HttpResponseRedirect(reverse('frontend:files'))
    return render(request, 'base_view.html', {'form': form})