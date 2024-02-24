from django.shortcuts import render


def view_tutorials(request):
    """ A view that renders the tutorials page  """
    return render(request, 'tutorials/tutorials.html')
