

# Create your models here.
from django.db import models

from django.contrib.auth.models import User

from email.policy import default




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username
class Customer(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    tin_no = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    tin_no = models.CharField(max_length=15, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=100, null=True) 
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=120)
    amount = models.PositiveBigIntegerField(default=0)
    supplier = models.ForeignKey(Supplier,  on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    initial_amount = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
         return self.name

class Order(models.Model):
    order_status_choices = (
        ('Loan_issue_Pending', 'Loan_issue_Pending'),
        ('Purchasing_issue_pending', 'Purchasing_issue_pending'),
        ('Issued', 'Issued')    
    )
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(Item,  on_delete=models.CASCADE, null=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    order_status= models.CharField(max_length=100, choices=order_status_choices, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} ordered quantity {self.order_quantity}"  
    
class IssueItem(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    issued_amount = models.PositiveIntegerField( default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    issued_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    issued_to = models.ForeignKey(Customer,  on_delete=models.CASCADE, null=True)
    issued_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()
    
    
    def __str__(self):
        return f'{self.item} - {self.issued_to}'
    
class ReturnItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    returned_date = models.DateTimeField(auto_now_add=True)
    returned_amount = models.PositiveIntegerField()
    #all_items_returned = models.BooleanField(default=False)
    returned_by = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.item} - {self.returned_by}'
    
class RestockItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    initial_value = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
        


