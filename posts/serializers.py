from rest_framework import serializers

from authentication.serializers import Account, AccountSerializer
from posts.models import Post, Product, Customer, CustomerOrder, OrderItem



class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']
    

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        
        
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Customer
        
     
        

        
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    
    #product = ProductSerializer(read_only=True)
    
    class Meta:
        model = OrderItem 
        
class CustomerOrderSerializer(serializers.HyperlinkedModelSerializer):
    orderItems = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomerOrder
#        fields = ('description', 'order', 'orderItems')


class FullCustomerSerializer(serializers.ModelSerializer):
    
    customerOrders = CustomerOrderSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'customerOrders')
        



