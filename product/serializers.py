from rest_framework import serializers 
from django.db.models import Avg

from .models import Product, Comment, Like

from .models import Product, Comment, Favorites

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['favorites'] = FavoritesSerializer(instance.favorites.all(), many=True).data
        return repr

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('product',)

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['product'] = ProductListSerializer(instance.post).data
        return repr
    
class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product 
        fields = ('title', 'price', 'image', 'document')
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        repr['reviews'] = instance.reviews.count()
        return repr


class CommentSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='User.username')
    owner = serializers.ReadOnlyField(source='owner.email')
    # owner = serializers.SerializerMethodField("get_owner")
    #
    # def get_owner(self, obj):
    #     return obj.owner.username
    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'product')
    def is_liked(self, product):
        user = self.context.get('request').user
        return user.liked.filter(product=product).exists()

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        # repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        user = self.context.get('request').user
        if user.is_authenticated:
            repr['is_liked'] = self.is_liked(instance)
        repr['likes_count'] = instance.likes.count()
        return repr



class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Like
        fields = ('owner',)