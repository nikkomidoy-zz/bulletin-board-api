from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from boards.models import Board
from posts.models import Post
from posts.serializers import PostSerializer
from threads.serializers import ThreadSerializer


class BoardSerializer(WritableNestedModelSerializer):
    threads = serializers.SerializerMethodField('get_threads')
    posts = serializers.SerializerMethodField('get_posts')

    class Meta:
        model = Board
        fields = ('name', 'description', 'is_draft', 'threads', 'posts',)

    def get_threads(self, board):
        return ThreadSerializer(
            instance=board.threads.all(), many=True
        ).data

    def get_posts(self, board):
        posts = Post.objects.filter(thread__in=board.threads.all())
        return PostSerializer(
            instance=posts, many=True
        ).data
