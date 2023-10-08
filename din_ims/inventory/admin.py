

# Register your models here.
from django.contrib import admin

from .models import UserProfile,ReturnItem,Item,RestockItem,IssueItem,Category,Supplier,Customer,Order
from django.urls import path
admin.site.site_header = "Inventory Admin"



# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "physical_address", "mobile", "picture")
    list_filter = ["user"]
    search_fields = ["user"]
    
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("name", "status", "description", "date_added")
    list_filter = ["name"]
    search_fields = ["name"]
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = ("name", "address", "phone" ,"tin_no", "email")
    list_filter = ["name", "phone"]
    search_fields = ["product"]   
    
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ("name", "address", "phone", "email")
    list_filter = ["name", "phone"]
    search_fields = ["product_code", "name"]
    
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ("name", "amount")
    list_filter = ["name"]
    search_fields = ["name"]
    
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ("customer", "name", "category", "selling_price", "created_by", "order_quantity", "date")
    list_filter = ["name"]
    search_fields = ["name"]    
    
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(IssueItem)
admin.site.register(ReturnItem)
admin.site.register(RestockItem)