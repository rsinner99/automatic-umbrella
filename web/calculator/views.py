from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status

from . import tasks
from web.serializers import TaskSerializer

class CalcView(GenericAPIView):
    serializer_class = TaskSerializer
    
    def post(self, request):
        result = tasks.estimate_pi.delay()
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')
