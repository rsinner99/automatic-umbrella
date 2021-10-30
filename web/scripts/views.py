import json

from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from web.serializers import TaskSerializer
from .models import Doc, Peer
from .serializers import DocSerializer, PeerSerializer
from . import tasks

# Create your views here.

MISSING_HOSTNAME = {
    'detail': 'Please provide hostname as query parameter'
}
MISSING_DOC = {
    'detail': 'Please provide doc ID as query parameter'
}

class DocViewSet(ModelViewSet):
    serializer_class = DocSerializer
    queryset = Doc.objects.all()

class PeerViewSet(ModelViewSet):
    serializer_class = PeerSerializer
    queryset = Peer.objects.all()

class ScriptView(GenericAPIView):
    serializer_class = TaskSerializer
    
    def post(self, request):
        hostname = request.query_params.get('hostname', None)
        doc = request.query_params.get('doc', None)
        if not hostname:
            return HttpResponse(json.dumps(MISSING_HOSTNAME), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        if not doc:
            return HttpResponse(json.dumps(MISSING_DOC), status=status.HTTP_400_BAD_REQUEST, content_type='application/json')

        host_list = hostname.split(',')
        peer = Peer.objects.filter(hostname__in=host_list).values_list('pk', flat=True)
        result = tasks.run_script.delay(doc, list(peer))
        resp = {
            'id': result.id,
            'state': result.state
        }
        return HttpResponse(json.dumps(resp), status=status.HTTP_200_OK, content_type='application/json')