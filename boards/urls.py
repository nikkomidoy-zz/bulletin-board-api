from rest_framework_extensions.routers import ExtendedDefaultRouter

from boards.views import BoardViewSet
from threads.views import ThreadViewSet

router = ExtendedDefaultRouter()

board_router = router.register('', BoardViewSet, basename='boards')
board_router.register(
    'threads',
    ThreadViewSet,
    basename='boards-threads',
    parents_query_lookups=['board',]
)

urlpatterns = router.urls
