import json

from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status

from . import tasks
from .serializers import TaskSerializer

class HelloView(GenericAPIView):
    serializer_class = TaskSerializer
    
    def post(self, request):
        input = request.query_params.get('input', 'Test')
        result = tasks.say_hello.delay(input)
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')
