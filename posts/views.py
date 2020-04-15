from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from posts.filters import PostFilter
from posts.models import Post
from posts.serializers import PostSerializer
from utils.views import CacheResponseAndETAGMixin


class PostViewSet(NestedViewSetMixin,
                  CacheResponseAndETAGMixin,
                  viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
