from django.shortcuts import render
import django_filters
from rest_framework import filters
from rest_framework import permissions, viewsets, authentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from posts.models import Post, Customer, CustomerOrder, Product, OrderItem
from posts.permissions import IsAuthorOfPost
from posts.serializers import PostSerializer, CustomerSerializer, \
    CustomerOrderSerializer, ProductSerializer, OrderItemSerializer, \
    FullCustomerSerializer, AllProductSerializer


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 5
    
    
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        return super(PostViewSet, self).perform_create(serializer)



class AccountPostsViewSet(viewsets.ViewSet):
    queryset = Post.objects.select_related('author').all()
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
    

class CustomerViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class FullCustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Customer.objects.all()
    serializer_class = FullCustomerSerializer
    
    
class CustomerOrderViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    
    
        


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')
    class Meta:
        model = Product
        fields = [ 'min_price', 'max_price']

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        return super(PostViewSet, self).perform_create(serializer)

class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter
    
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 100000
    
class AllProductViewSet(ProductViewSet):
    pagination_class = LargeResultsSetPagination
    serializer_class = AllProductSerializer
    
    

    
    
    