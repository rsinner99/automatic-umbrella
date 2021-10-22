from rest_framework.serializers import ModelSerializer, Serializer

from .views import Doc, Peer

class DocSerializer(ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'

class PeerSerializer(ModelSerializer):
    class Meta:
        model = Peer
        fields = '__all__'

class TaskSerializer(Serializer):
    class Meta:
        ref_name = 'Task'
        fields = '__all__'
        