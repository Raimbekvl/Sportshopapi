from rest_framework.routers import SimpleRouter
from django.urls import path 
from . import views 

router = SimpleRouter()

urlpatterns = [
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]