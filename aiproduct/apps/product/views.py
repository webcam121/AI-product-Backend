from rest_framework.response import Response
from rest_framework import filters, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView

from .models import Product, ProductClick, UserUtmParameter, Category
from .serializers import ProductSerializer, AiProductClickSerializer, UserUtmParameterSerializer, CategorySerializer
from .filters import ProductFilter
from django.http import HttpResponseRedirect
from aiproduct.apps.product import tasks


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'url', 'image_url']
    ordering_fields = ['created_at']


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateAiProductClickView(APIView):
    serializer_class = AiProductClickSerializer

    def get(self, request, *args, **kwargs):
        click_source = request.GET.get('click_source')
        uid = request.GET.get('uid')
        product = Product.objects.get(id=self.kwargs.get('id'))
        # tasks.process_product_click_events.delay(
        #     product_id=product.pk,
        #     uid=uid,
        #     click_source=click_source,
        # )

        filter_kwargs = {'uid': uid}
        has_clicked_product = ProductClick.objects.filter(
            product=product,
            **filter_kwargs,
        ).exists()
        if not has_clicked_product:
            ProductClick.objects.create(
                uid=uid,
                click_source=click_source,
                product=product,
            )

        product_url = product.url

        return Response(product_url, status=status.HTTP_200_OK)


class CreateUserUtmParameterView(generics.CreateAPIView):
    serializer_class = UserUtmParameterSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserUtmParameterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user_utm, created = UserUtmParameter.objects.get_or_create(
            uid=data['uid'],
            ctime=data['ctime'],
            utm_campaign=data['utm_campaign'],
            utm_content=data['utm_content'],
            utm_medium=data['utm_medium'],
            utm_source=data['utm_source'],
            client_ip_address=data['client_ip_address'],
            client_user_agent=data['client_user_agent'],
            source_url=data['source_url'],
            utm_term=data['utm_term'],
            fbclid=data['fbclid'],
            gclid=data['gclid'],
            gbraid=data['gbraid'],
            wbraid=data['wbraid'],
            irclickid=data['irclickid'],
            blogsource=data['blogsource'],
            ttclid=data['ttclid'],
            sccid=data['sccid'],
        )

        if created:
            return Response(UserUtmParameterSerializer(user_utm).data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "UTM parameters already exists."}, status=status.HTTP_200_OK)


class ProductsByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        categories = self.request.query_params.get('categories', None)
        if categories is not None:
            categories = categories.split(',')
            return Product.objects.filter(category__id__in=categories)
        else:
            return Product.objects.none()


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    pagination_class = None