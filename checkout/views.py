from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OTK3hIfNWYlwh3BnTJxEGd70J2wJHQOpV5iFfMr2hxexbDYuutr2taUytDCe9R5w83Kf0DoFVsCWbFbORe73VNs00dBJ3KzIr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    