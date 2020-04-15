from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from bulletin_board.users.permissions import IsAdministratorOnly
from threads.models import Thread
from threads.serializers import ThreadSerializer
from utils.views import CacheResponseAndETAGMixin


class ThreadViewSet(NestedViewSetMixin,
                    CacheResponseAndETAGMixin,
                    viewsets.ModelViewSet):

    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    @action(detail=True, methods=['post',], permission_classes=[IsAdministratorOnly,])
    def mark_as_sticky(self, request, pk):
        thread = self.get_object()
        thread.is_sticky = True
        thread.save()
        return Response({'status': f'{thread} marked as sticky'})
