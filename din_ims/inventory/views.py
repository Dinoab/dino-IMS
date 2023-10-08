
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddItemForm, UpdateItemForm,ReturnItemForm,RestockItemForm,IssueItemForm,SupplierForm,CustomerForm,CategoryForm,OrderForm
from .models import Item,RestockItem,IssueItem,ReturnItem,Customer,Category,Supplier,Order,User
from django.core.paginator import Paginator

@login_required
def index(request):
    orders_user = Order.objects.all()
    users = User.objects.all()[:2]
    orders_adm = Order.objects.all()[:2]
    items = Item.objects.all()[:2]
    reg_users = len(User.objects.all())
    all_items = len(Item.objects.all())
    all_orders = len(Order.objects.all())
    all_customers = len(Customer.objects.all())

    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "items": items,
        "count_users": reg_users,
        "count_items": all_items,
        "count_orders": all_orders,
        "count_customers":all_customers,
    }

    return render(request, "inventory/index.html", context)

@login_required
def users(request):
    users = User.objects.all()
    context = {"title": "Users", "users": users}
    return render(request, "inventory/users.html", context)

@login_required
def user(request):
    context = {"profile": "User Profile"}
    return render(request, "inventory/user.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistry()
    context = {"register": "Register", "form": form}
    return render(request, "inventory/register.html", context)


@login_required
def suppliers(request):
    suppliers = Supplier.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suppliers")
    else:
        form = SupplierForm()
    context = {"title": "suppliers", "suppliers": suppliers, "form": form}
    return render(request, "inventory/suppliers.html", context)

@login_required
def customers(request):
    customers = Customer.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers")
    else:
        form = SupplierForm()
    context = {"title": "customers", "customers": customers, "form": form}
    return render(request, "inventory/customers.html", context)
@login_required

def category(request):
    category = Category.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("category")
    else:
        form = CategoryForm()
    context = {"title": "Category", " categories": category, "form": form}
    return render(request, "inventory/category.html", context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.initial_amount = var.amount
            var.save()
            messages.info(request, 'New Item has been added  to your store')
            return redirect('all-items')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('add-item')
    else:
        form = AddItemForm()
        context = {'form': form}
        return render(request, 'inventory/add_item.html', context)
    
@login_required
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item has been updated  successfully')
            return redirect('all-items')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateItemForm(instance=Item)
        context = {'form': form}
        return render(request, 'inventory/update_item.html', context)   

@login_required
def all_items(request):
    items = Item.objects.all().order_by('-created_date')
    context = {'items':items}
    return render(request, 'inventory/products.html', context)
@login_required
def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    messages.info(request, 'Item has been Deleted Successfully')
    return redirect('all-items')

@login_required
def orders(request):
    orders = Order.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()
    context = {"title": "Orders", "orders": orders, "form": form}
    return render(request, "inventory/orders.html", context)
@login_required
def issue_item(request):
    if request.method == 'POST':
        form = IssueItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.issued_by = request.user
            get_item = Item.objects.get(pk=var.item.pk)
            
            if get_item.amount != 0: 
                if get_item.amount > var.issued_amount:
                    get_item.amount = get_item.amount - var.issued_amount
                    get_item.save()
                    var.save()
                    messages.info(request, f'Item has been issued to {var.issued_to} successfully')
                    return redirect('all-items')
                else:
                    messages.info(request, f'We have no requested amount!  We had only {get_item.amount} left!')
                    return redirect('all-items')     
            else:
                    messages.info(request, f'We have no requested amount!')
                    return redirect('all-items')         
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('issue-item')
    else:
        form = IssueItemForm(instance=Item)
        context = {'form': form}
        return render(request, 'inventory/issue_item.html', context)
@login_required
def issue_history(request):
    items = IssueItem.objects.all().order_by('-issued_date')
    context = {'items':items}
    return render(request, 'inventory/issue_history.html', context)

@login_required
def return_item(request):
    if request.method == 'POST':
        form = ReturnItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            get_item = Item.objects.get(pk=var.item.pk)
            get_item.amount = get_item.amount + var.returned_amount
            if get_item.amount > get_item.initial_amount:
                    messages.warning(request, f'Items returned are more than initial amount ({get_item.initial_amount})we had in store')
                    return redirect('all-items')
            else:
                get_item.save()
                var.save()
                messages.info(request, 'The Item has been returned  back to the store successfully')
                return redirect('all-items')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('all-items') 
    else:
        form = IssueItemForm(instance=Item)
        context = {'form': form}
        return render(request, 'inventory/return_item.html', context)

@login_required
def return_history(request):
    items = ReturnItem.objects.all()
    context = {'items':items}
    return render(request, 'inventory/return_history.html', context)
@login_required
def restock_item(request):
    if request.method == 'POST':
        form = RestockItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            get_item = Item.objects.get(pk=var.item.pk)
            var.initial_value = get_item.initial_amount
            get_item.initial_amount = get_item.initial_amount + var.amount
            get_item.save()
            var.save()
            messages.info(request, 'Item has been restocked to store successfully')
            return redirect('all-items')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('restock-item')
    else:
        form = RestockItemForm(instance=Item)
        context = {'form': form}
        return render(request, 'inventory/restock_item.html', context)   

@login_required
def restock_history(request):
    items = RestockItem.objects.all().order_by('-timestamp')
    context = {'items':items}
    return render(request, 'inventory/restock_history.html', context)

@login_required()
def dashboard(request):
    items = Item.objects.all()
    df = read_frame(items)
        # best performing product
    best_performing_product_df = df.groupby(by="name").sum().sort_values(by="issued_amount")
    best_performing_product = px.bar(best_performing_product_df, 
                                    x = best_performing_product_df.index, 
                                    y = best_performing_product_df.issued_amount, 
                                    title="Best Performing Product"
                                )
    best_performing_product = json.dumps(best_performing_product, cls=plotly.utils.PlotlyJSONEncoder)



     # Most Product In Stock
    most_product_in_stock_df = df.groupby(by="name").sum().sort_values(by="initial_value")
    most_product_in_stock = px.pie(most_product_in_stock_df, 
                                    names = most_product_in_stock_df.index, 
                                    values = most_product_in_stock_df.quantity_in_stock, 
                                    title="Most Product In Stock"
                                )
    most_product_in_stock = json.dumps(most_product_in_stock, cls=plotly.utils.PlotlyJSONEncoder)

    context = {
        "sales_graph": sales_graph,
        "best_performing_product": best_performing_product,
        "most_product_in_stock": most_product_in_stock,
        "best_performing_product_per_product": best_performing_product_per_product
    }

    return render(request,"inventory/dashboard.html", context=context)