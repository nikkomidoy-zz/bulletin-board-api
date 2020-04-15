from rest_framework_extensions.routers import ExtendedDefaultRouter

from posts.views import PostViewSet
from threads.views import ThreadViewSet

router = ExtendedDefaultRouter()

thread_router = router.register('', ThreadViewSet, basename='threads')
thread_router.register(
    'posts',
    PostViewSet,
    basename='thread-post',
    parents_query_lookups=['thread',]
)

urlpatterns = router.urls
