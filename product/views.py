from rest_framework.viewsets import ModelViewSet 
from rest_framework import permissions, response
from rest_framework.decorators import action 
from rating.serializers import ReviewSerializer
from .import serializers
from .models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)

    def get_serializer_class(self):
        if self.action =='list':
            return serializers.ProductListSerializer
        return serializers.ProductDetailSerializer

    #api/v1/products/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data
            return response.Response(serializer, status=200)
        data = request.data 
        serializer = ReviewSerializer(data=data, context={'request': request, 'product': product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201) 
