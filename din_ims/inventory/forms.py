from django import forms
from .models import Item, IssueItem, RestockItem, ReturnItem,Supplier,Customer, Category,Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "address", "phone" ,"tin_no", "email"]   
        
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "address", "phone" , "email"] 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "status", "description"]

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'amount','category', 'supplier', 'price']
        
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [  "customer", "category", "name" ,"selling_price", "order_quantity",'order_status']
class IssueItemForm(forms.ModelForm):
    class Meta:
        model = IssueItem
        fields = ['item','issued_amount','selling_price','issued_to', 'return_date']
        
        
class ReturnItemForm(forms.ModelForm):
    class Meta:
        model = ReturnItem
        fields = ['item', 'returned_amount', 'returned_by']
class RestockItemForm(forms.ModelForm):
    class Meta:
        model = RestockItem
        fields = ['item', 'amount']  
