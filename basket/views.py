from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    options = None
    if 'product_options' in request.POST:
        options = request.POST['product_options']
    basket = request.session.get('basket', {})

    if options:
        if item_id in list(basket.keys()):
            if options in basket[item_id]['items_by_options'].keys():
                basket[item_id]['items_by_options'][options] += quantity
            else:
                basket[item_id]['items_by_options'][options] = quantity
        else:
            basket[item_id] = {'items_by_options': {options: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    options = None
    if 'product_options' in request.POST:
        options = request.POST['product_options']
    basket = request.session.get('basket', {})

    if options:
        if quantity > 0:
            basket[item_id]['items_by_options'][options] = quantity
        else:
            del basket[item_id]['items_by_options'][options]
            if not basket[item_id]['items_by_options']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        # product = get_object_or_404(Product, pk=item_id)
        options = None
        if 'product_options' in request.POST:
            options = request.POST['product_options']
        basket = request.session.get('basket', {})

        if options:
            del basket[item_id]['items_by_options'][options]
            if not basket[item_id]['items_by_options']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
