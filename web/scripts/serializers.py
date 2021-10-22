from rest_framework.serializers import ModelSerializer

from .views import Doc, Peer

class DocSerializer(ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'

class PeerSerializer(ModelSerializer):
    class Meta:
        model = Peer
        fields = '__all__'
