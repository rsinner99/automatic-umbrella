from rest_framework.serializers import Serializer

class TaskSerializer(Serializer):
    class Meta:
        ref_name = 'Task'
        fields = '__all__'
        