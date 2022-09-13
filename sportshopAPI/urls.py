"""sportshopAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from product import views
from product.views import ProductViewSet, home
from django.conf.urls.static import static
from django.conf import settings
from cart.views import CartApiView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from product import views

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



router = SimpleRouter()
router.register('products', ProductViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Sport_Shop API",
      default_version='v1',
      description="test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/cart/', CartApiView.as_view()),
    path('api/v1/orders/', include('order.urls')),
    url(r'^$', views.home, name='product.urls'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),

]
# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
#     url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
#     url(r'^admin/', admin.site.urls),
# ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)