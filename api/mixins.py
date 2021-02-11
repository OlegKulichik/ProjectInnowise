from rest_framework.decorators import action
from rest_framework.response import Response

from likes import services

from .serializers import UserSerializer


class LikedMixin:
       
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Like a model instance.
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Unlike a model instance.
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def fans(self, request, pk=None):
        """Get the users which liked a model instance.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)