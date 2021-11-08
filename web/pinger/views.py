from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status

from . import tasks
from web.serializers import TaskSerializer

class PingView(GenericAPIView):
    serializer_class = TaskSerializer
    
    def post(self, request):
        host = request.query_params.get('host', '')
        timeout = float(request.query_params.get('timeout', 2))
        result = tasks.ping_host.delay(host, timeout)
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')
