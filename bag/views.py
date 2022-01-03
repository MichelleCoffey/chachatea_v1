from django.shortcuts import render

def view_bag(request):
    """ A view to render the shapping bag. """

    return render(request, 'bag/bag.html')
