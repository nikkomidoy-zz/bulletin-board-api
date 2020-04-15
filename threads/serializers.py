from drf_writable_nested import WritableNestedModelSerializer

from threads.models import Thread


class ThreadSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'
