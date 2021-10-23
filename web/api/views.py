import json

from celery.result import AsyncResult

from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.generics import GenericAPIView
from rest_framework import status

from web.serializers import TaskSerializer
from web.utils import reverse
from scripts.views import ScriptView
from storage.views import FileView

MISSING_TASK_ID = {
    'detail': 'Please provide task id as query parameter "task"'
}

class ApiTaskView(GenericAPIView):
    serializer_class = TaskSerializer

    def get(self, request):
        task_id = request.query_params.get('task', None)
        if not task_id:
            return HttpResponse(json.dumps(MISSING_TASK_ID), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        
        task = AsyncResult(task_id)
        result = task._get_task_meta()
        if not result.get('task_id'):
            result['task_id'] = task_id

        return HttpResponse(json.dumps(result), status=status.HTTP_200_OK, content_type='application/json')

    
class ApiScriptView(ScriptView):
    def post(self, request):
        response = super().post(request)
        result = json.loads(response.content)

        task_id = result.get('id', None)
        if not task_id:
            return response
        return HttpResponseRedirect(reverse('api-task-result', get={'task': task_id}))


class ApiFileView(FileView):
    def get(self, request):
        response = super().post(request)
        result = json.loads(response.content)

        task_id = result.get('id', None)
        if not task_id:
            return response
        return HttpResponseRedirect(reverse('api-task-result', get={'task': task_id}))
