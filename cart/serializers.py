from .models import Cart
from product.models import Product

#REST_FRAMEWORK
from rest_framework import serializers, generics

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(pk=attrs['product'])

        except Product.DoesNotExist:
            raise serializers.ValidationError('Product not found')
        count = attrs['count']
        data['count'] = count
        data['product'] = product.pk

        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Cart.objects.create(
            product=product,
            user=user,
            count=data['count']
        )


