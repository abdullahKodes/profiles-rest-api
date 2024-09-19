from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
        'Uses Http methods as functions (get, post, put, patch, delete)',
        'is similar to Django Views'
        ]

        return Response({'message':'Hello World', 'an_apiview': an_apiview})
