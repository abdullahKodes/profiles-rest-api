from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes the name field to test our APIView"""
    name = serializers.CharField(max_length=10)
