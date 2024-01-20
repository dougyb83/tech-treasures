from django.shortcuts import render, redirect


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
