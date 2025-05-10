from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Create your views here.

# Index
def index_p(request):
    return render(request,'base.html')

# Create
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

# Read
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# Update
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/update_product.html', {'form': form})

# Delete
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/delete_product.html', {'product': product})
