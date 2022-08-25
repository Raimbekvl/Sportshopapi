# REST FRAMEWORK
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Cart
from . import serializers

class CartApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = serializers.CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

    def get(self, request):
        carts = Cart.objects.all()
        serializer = serializers.CartListSerializer(carts, many=True).data
        return Response(serializer, status=200)
