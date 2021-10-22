import json

from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status

from web.serializers import TaskSerializer
from . import tasks

MISSING_FILENAME = {
    'detail': 'Please provide filename as query parameter'
}

MISSING_CONTENT_OR_PATH = {
    'detail': 'Please provide either content or filepath as query parameter'
}

class FileView(GenericAPIView):
    serializer_class = TaskSerializer

    def get(self, request):
        filename = request.query_params.get('filename', None)
        if not filename:
            return HttpResponse(json.dumps(MISSING_FILENAME), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

        result = tasks.get_content.delay(filename)
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')
        
    
    def post(self, request):
        filename = request.query_params.get('filename', None)
        if not filename:
            return HttpResponse(json.dumps(MISSING_FILENAME), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        content = request.query_params.get('content', None)
        filepath = request.query_params.get('filepath', None)
        if content:
            result = tasks.put_content.delay(filename, content)
        elif filepath:
            result = tasks.put_file.delay(filename, filepath)
        else:
            return HttpResponse(json.dumps(MISSING_CONTENT_OR_PATH), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')
