from rest_framework_extensions.routers import ExtendedDefaultRouter

from posts.views import PostViewSet

router = ExtendedDefaultRouter()

router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
