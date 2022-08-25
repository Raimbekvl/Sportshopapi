from .models import *
from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product.title')
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'product_title')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr.pop('product')
        return repr


class OrderSerializer(serializers.ModelSerializer):
    # positions = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Order
        fields = ('id', 'created_at', 'user', 'status')

    def create(self, validated_data):
        products = validated_data
        # products = validated_data.pop('positions')
        user = self.context.get('request').user
        order = Order.objects.create(user=user, status='open')
        for prod in products:
            product = prod['product']
            quantity = prod['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        return order

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['products'] = OrderItemSerializer(instance.items.all(), many=True).data
        return repr
