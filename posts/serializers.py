from drf_writable_nested import WritableNestedModelSerializer

from posts.models import Post


class PostSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
