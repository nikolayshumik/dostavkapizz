from django.shortcuts import render, redirect
from .models import Pizza, Order
from .forms import OrderForm

def pizza(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizza.html', {'pizzas': pizzas})

def order(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.save()
            return redirect('order_complete')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'pizza': pizza})

def order_complete(request):
    return render(request, 'order_complete.html')

def cookers(request):
    orders = Order.objects.all()
    return render(request, 'cookers.html', {'orders': orders})