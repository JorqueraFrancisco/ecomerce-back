from django.urls import include, path
from store_admin import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'admin-user', views.UserViewSet)
# router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path(r'product/<int:product_id>/', views.ProductView.as_view()),
    path(r'product/', views.ProductView.as_view()),
    path(r'file/<int:file_id>/', views.FileView.as_view()),
]
