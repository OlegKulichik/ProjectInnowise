from rest_framework.decorators import action
from rest_framework.response import Response

from likes import services
from match import services

from .serializers import UserSerializer



class LikedMixin:
       
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """
        Like a model instance
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()
    
    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """
        Unlike a model instance
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()
    
    @action(detail=True, methods=["GET"])
    def voted_persons(self, request, pk=None):
        """
        Get person that liked
        """
        obj = self.get_object()
        voted_persons = services.get_voted_persons(obj)
        serializer_context = {"request": request}
        serializer = UserSerializer(
            voted_persons, many=True, context=serializer_context
        )
        
        return Response(serializer.data)


class MatchMixin:

    @action(detail=True, methods=["GET"])
    def voted_persons(self, request, pk=None):
        """
        Get person that match 'obj'
        """
        obj = self.get_object()
        voted_persons = services.get_voted_persons(obj)
        serializer_context = {"request": request}
        serializer = UserSerializer(
            voted_persons, many=True, context=serializer_context
        )

        return Response(serializer.data)

