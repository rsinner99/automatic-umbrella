import json

from celery.result import AsyncResult
from celery.execute import send_task 

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework import status

from web.serializers import TaskSerializer
from web.utils import reverse
from hello import tasks as hello
from scripts.views import ScriptView
from storage.views import FileView
from frontend.models import Task

MISSING_TASK_ID = {
    'detail': 'Please provide task id as query parameter "task"'
}

class ApiTaskView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        task_id = request.query_params.get('task', None)
        if not task_id:
            return HttpResponse(json.dumps(MISSING_TASK_ID), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        
        task = AsyncResult(task_id)
        result = task._get_task_meta()
        if not result.get('task_id'):
            result['task_id'] = task_id

        return HttpResponse(json.dumps(result), status=status.HTTP_200_OK, content_type='application/json')

class ApiTaskUpdateView(GenericAPIView):
    serializer_class = TaskSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        task_id = request.query_params.get('task', None)
        state = request.query_params.get('state', None)
        name = request.query_params.get('name', None)

        try:
            task = Task.objects.get(task_id=task_id)
            task.task_name=name
            task.state=state
            task.save()
        except Task.DoesNotExist:
            task = Task.objects.create(
                task_id=task_id,
                task_name=name,
                state=state
            )
        return HttpResponse("Created/ Updated", status=status.HTTP_200_OK)


class ApiScriptStoreView(GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        kwargs = request.query_params
        doc = int(kwargs.get('doc'))
        peers = kwargs.get('peers').split(',')
        filename = kwargs.get('filename')
        result = hello.run_script_output_to_storage.delay(doc, peers, filename)
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')

    
class ApiScriptView(ScriptView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = super().post(request)
        result = json.loads(response.content)

        task_id = result.get('id', None)
        if not task_id:
            return response
        return HttpResponseRedirect(reverse('api-task-result', get={'task': task_id}))


class ApiFileView(FileView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        response = super().get(request)
        result = json.loads(response.content)

        task_id = result.get('id', None)
        if not task_id:
            return response
        return HttpResponseRedirect(reverse('api-task-result', get={'task': task_id}))

@login_required
def run_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        taskname = data.pop('taskname')
        result = send_task(taskname, kwargs=data)
        response = {
            'task_id': result.id
        }
        Task.objects.create(
            task_id=result.id,
            task_name=taskname,
            user=request.user
        )
        return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)
    else:
        response = {
            'detail': request.method + " is not allowed"
        }
        return HttpResponse(json.dumps(response), status=status.HTTP_405_METHOD_NOT_ALLOWED)