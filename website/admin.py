from django.contrib import admin
from .models import ContactMessage, Destination, Hotel, Package, Flight, Testimonial
# Register your models here.

models_list = [
    ContactMessage,
    Destination,
    Hotel,
    Package,
    Flight,
    Testimonial,
]

def register_models(models):
    admin.site.register(models)

register_models(models_list)