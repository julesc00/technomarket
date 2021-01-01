from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        "title": "Tecnomarket",
        "welcome": "Welcome to my badd-ass market!",
        "products": products
    }
    return render(request, "app/home.html", context)


def contact(request):
    context = {
        "welcome": "This is the Contact Page"
    }
    return render(request, "app/contact.html", context)


def gallery(request):
    context = {
        "welcome": "This is the gallery"
    }
    return render(request, "app/gallery.html", context)
