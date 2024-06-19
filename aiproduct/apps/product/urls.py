from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('<int:id>/click/', views.CreateAiProductClickView.as_view(), name='product-click'),
    path('create-utm-param/', views.CreateUserUtmParameterView.as_view(), name='utm-parameter'),
    path('products-by-category/', views.ProductsByCategoryView.as_view(), name='products_by_category'),
    path('category/', views.CategoryList.as_view(), name='category')
]
