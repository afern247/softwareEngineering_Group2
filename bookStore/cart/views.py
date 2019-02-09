# =====================================================
# CODE AUTHOR: RAUL ESPINOSA
# The views for the Cart. I used the Django
# documentation to learn about views:

# https://docs.djangoproject.com/en/2.1/topics/http/views/
# https://docs.djangoproject.com/en/2.1/ref/views/

# EDIT: Don't know why, but my last push from when I was working in my branch
# didn't push either this or my forms.py file to the Development branch.
# =====================================================

from django.shortcuts import render, redirect, get_object_or_404
# We will need this for views that intend to change data; those
# require HTTP POST requests.
from django.views.decorators.http import require_POST

# These are the cart and cart forms.
from bookStore.cart.cart import Cart
from bookStore.cart.forms import AddToCartForm
# This is the TEMPORARY Book model that I created
# to be used with the cart.
from cart.models import Book


# This is the view that will handle adding/updating items


@require_POST
def addToCart(request, book_name):
    userCart = Cart(request)
    # Attempt to get the Book that has the
    # given book name
    book = get_object_or_404(Book, name=book_name)

    # Validate the form for adding the item to the cart
    form = AddToCartForm(request.POST)

    # If the form is successfully validated, we
    # proceed with adding to/updating the book's
    # amount in the cart
    if form.is_valid():
        data = form.cleaned_data
        userCart.add(book=book,
                     amount=data['amount'],
                     change_amount=data['change_amount'])

    # Once finished, the function redirects the user to the page
    # that shows them the contents of their cart
    return redirect('userCart:cart_info')

# This view will handle removing items.


def removeFromCart(request, book_name):
    userCart = Cart(request)
    # Same as addToCart function
    book = get_object_or_404(Book, name=book_name)

    # Simply remove the Book with the given name
    # from the cart
    userCart.remove(book)

    # Again, redirect to cart contents page
    return redirect('userCart:cart_info')


# This view displays the cart and its contents

def cart_info(request):
    userCart = Cart(request)
    return render(request, 'cart/info.html', {'userCart': userCart})