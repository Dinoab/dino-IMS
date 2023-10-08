from django.urls import path
from . import views

from django.contrib import admin


urlpatterns = [
    path("register/", views.register, name="register"),
    path("user/", views.user, name="user"),
    path("users/", views.users, name="users"),
    path("dash/", views.index, name="dash"),
    path("category/", views.category, name="category"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("customers/", views.customers, name="customers"),
    path("orders/", views.orders, name="orders"),
    
    
    path('add-item/', views.add_item, name='add-item'),
    path('update-item/<int:pk>/', views.update_item, name='update-item'),
    path('all-items/', views.all_items, name='all-items'),
    path('delete-item/<int:pk>/', views.delete_item, name='delete-item'),
    path('issue-item/', views.issue_item, name='issue-item'),
    path('issue-history/', views.issue_history, name='issue-history'),
    path('return-item/', views.return_item, name='return-item'),
    path('return-history/', views.return_history, name='return-history'),
    path('restock-item/', views.restock_item, name='restock-item'),
    path('restock-history/', views.restock_history, name='restock-history'),
]