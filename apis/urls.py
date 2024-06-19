from django.urls import include, path

app_name = 'apis'

urlpatterns = [
    path('product/', include('aiproduct.apps.product.urls', namespace='products')),
]
