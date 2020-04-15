from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    @action(detail=True, methods=['put', 'delete',])
    def following(self, request, pk):
        user_to_handle = self.get_object()

        if request.method == 'PUT':
            request.user.following.add(user_to_handle)
            return Response(
                {
                    'message': 'Now following {}'.format(
                        user_to_handle.get_full_name())
                }
            )

        if request.method == 'DELETE':
            request.user.following.remove(user_to_handle)
            return Response(
                {
                    'message': 'Unfollowed {}'.format(
                        user_to_handle.get_full_name())
                }
            )

    @action(detail=True, methods=['put', 'delete',])
    def ban(self, request, pk):
        user_to_handle = self.get_object()
        if request.method == 'PUT':
            user_to_handle.is_banned = True
            user_to_handle.save()
            return Response(
                {
                    'message': '{} is now banned.'.format(
                        user_to_handle.get_full_name())
                }
            )

        if request.method == 'DELETE':
            user_to_handle.is_banned = False
            user_to_handle.save()
            return Response(
                {
                    'message': '{} is now unbanned.'.format(
                        user_to_handle.get_full_name())
                }
            )

    @action(detail=True, methods=['GET'])
    def followers(self, request, pk):
        user_followers = User.objects.filter(following__in=[self.get_object()])
        user_serializer = UserSerializer(instance=user_followers, many=True)

        return Response(user_serializer.data)


    @action(detail=True, methods=['GET'])
    def following(self, request, pk):
        user_serializer = UserSerializer(
            instance=self.get_object().follwing.all(),
            many=True
        )

        return Response(user_serializer.data)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
