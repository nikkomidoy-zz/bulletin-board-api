from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from boards.models import Board
from boards.serializers import BoardSerializer
from bulletin_board.users.permissions import (IsAdministratorOnly,
                                              IsModeratorOnly)
from utils.views import CacheResponseAndETAGMixin


class BoardViewSet(NestedViewSetMixin,
                   CacheResponseAndETAGMixin,
                   viewsets.ModelViewSet):

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAdministratorOnly, IsModeratorOnly]
