from django.db import models

from authentication.models import Account


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}'.format(self.content)
    
    
    
class Product(models.Model):
    #author = models.ForeignKey(Account, null = True)
    description = models.TextField(null = True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name 
    
class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    
    def __str__(self):
        return self.firstName + " " + self.lastName 
    
    @property
    def name(self):
        return ''.join([self.lastname,' ,', self.firstName])

class CustomerOrder(models.Model):
    order = models.ForeignKey(Customer, related_name='customerOrders')
    description = models.TextField(null = False, blank = True, default= "")
    
    def __str__(self):
        #result = self.description if self.description else ""
        #return  self.description + ":" + self.order.__str__()
        return self.order.__str__()
    @property
    def name(self):
        return ''.join(
            [self.lastname,' ,', self.firstname, ' ', self.middlename])
    
    
class OrderItem(models.Model):
    customerOrder = models.ForeignKey(CustomerOrder, related_name='orderItems')
    product = models.ForeignKey(Product)
    qty = models.IntegerField(default = 1)
    
    
    