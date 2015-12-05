from rest_framework import serializers

from authentication.serializers import Account, AccountSerializer
from posts.models import Post, Product, Customer, CustomerOrder, OrderItem, \
    League, Game, Team, Location


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Post

        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        
        return exclusions + ['author']
    

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        

class AllProductSerializer(ProductSerializer):

    class Meta:
        model = Product
        fields = ('url', 'name', 'price', )       
        
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Customer
        
        
class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    
    #customerOrder = CustomerOrderSerializer(required=False)
    class Meta:
        model = OrderItem
        #fields = ('product', 'qty')
        exclude = ('customerOrder',)
        
    
        
class CustomerOrderSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    
    orderItems = OrderItemSerializer(many=True)
    
    class Meta:
        model = CustomerOrder
        
        #fields = ('description', 'order', 'orderItems')
    def create(self, validated_data):
        orderItems = validated_data.pop('orderItems')
        customerOrder = CustomerOrder.objects.create(**validated_data)
        for oi in orderItems:
            OrderItem.objects.create(customerOrder=customerOrder, **oi)
        return customerOrder

    
    def update(self, instance, validated_data):
        OrderItem.objects.filter(customerOrder=instance).delete()
        orderItems = validated_data.pop('orderItems')
        for oi in orderItems:
            OrderItem.objects.create(customerOrder=instance, **oi)
        return super(CustomerOrderSerializer, self).update( instance, validated_data)


class FullCustomerSerializer(serializers.ModelSerializer):
    
    customerOrders = CustomerOrderSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'customerOrders')
        


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Location
        
class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = League
        
        
class GameSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Game
        
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.CharField(source='__str__', read_only=True)
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Team
        
