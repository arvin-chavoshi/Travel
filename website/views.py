from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import ContactMessage, Destination, Hotel, Package, Flight, Testimonial
from django.contrib import messages
from blog.models import Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #--------------- get destination and posts ----------------------#
    destinations = Destination.objects.all()[:3]
    posts = Post.objects.filter(is_published=True).order_by("-views","-id")[:6]

    #--------------- get objects with type cheap luxury camping --------------------#
    cheap_objs = Package.objects.filter(package_type="cheap").order_by("-price_per_person","-id")
    luxury_objs = Package.objects.filter(package_type="luxury").order_by("-price_per_person","-id")
    camping_objs = Package.objects.filter(package_type="camping").order_by("-price_per_person","-id")

    #--------------- get testimonials ------------------------#
    testimonials = Testimonial.objects.filter(is_active=True)

    context = {
        "destinations" : destinations,
        "posts" : posts,
        "cheap" : cheap_objs,
        "luxury" : luxury_objs,
        "camping" : camping_objs,
        "testimonials" : testimonials,
    }

    return render(request, "website/index.html", context)

@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                subject = form.cleaned_data['subject'],
                message = form.cleaned_data['message'],
            )
            messages.success(request, "Your Message was sent successfully.")
            return redirect("website:contact")
    else :
        form = ContactForm()

    context = {
        "form" : form,
    }

    return render(request, "website/contact.html", context)

def about(request):
    #--------------- get objects with type cheap luxury camping --------------------#
    cheap_objs = Package.objects.filter(package_type="cheap").order_by("-price_per_person","-id")
    luxury_objs = Package.objects.filter(package_type="luxury").order_by("-price_per_person","-id")
    camping_objs = Package.objects.filter(package_type="camping").order_by("-price_per_person","-id")

    context = {
        "cheap" : cheap_objs,
        "luxury" : luxury_objs,
        "camping" : camping_objs,
    }

    return render(request, "website/about.html", context)

def elements(request):
    return render(request, "website/elements.html")

def destination_details(request, pk):
    destination_obj = get_object_or_404(Destination, pk=pk)

    context = {
        "destination_obj" : destination_obj,
    }

    return render(request, "website/destination_details.html", context)

def hotels(request):
    hotels = Hotel.objects.filter(is_active=True).order_by("-price_pernight","-id")

    #-------------------- hotels filter ------------------------#
    if request.method == "GET":
        hotel_name = request.GET.get("hotel_name")
        rating = request.GET.get("rating")
        swimmingpool = request.GET.get("swimmingpool")
        roomservice = request.GET.get("roomservice")
        pricestart = request.GET.get("price_start")
        priceend = request.GET.get("price_end")
        if hotel_name:
            hotels = hotels.filter(name__icontains=hotel_name)
        if rating:
            hotels = hotels.filter(Q(rating__lte=rating))
        if swimmingpool is not None:
            hotels = hotels.filter(swimming_pool=swimmingpool)
        if roomservice is not None:
            hotels = hotels.filter(room_service=roomservice)
        if pricestart:
            hotels = hotels.filter(Q(price_pernight__gte=pricestart))
        if priceend:
            hotels = hotels.filter(Q(price_pernight__lte=priceend))


    context = {
        "hotels" : hotels,
    }

    return render(request, "website/hotels.html", context)

def insurance(request):
    return render(request, "website/insurance.html")

def packages(request):
    packages_list = Package.objects.filter(is_active=True).order_by("-price_per_person","-id")
    hot_deals = packages_list.filter(is_hot_deal=True)

    #----------------- Packages Filter ----------------------#
    if request.method == "GET":
        country = request.GET.get("country")
        days = request.GET.get("days")
        nights = request.GET.get("night")
        date = request.GET.get("date")
        price = request.GET.get("price")
        airport = request.GET.get("airport")
        if country:
            packages_list = packages_list.filter(country__icontains=country)
        if days:
            packages_list = packages_list.filter(days__lte=days)
        if nights:
            packages_list = packages_list.filter(nights__lte=nights)
        if date:
            packages_list = packages_list.filter(date__gte=date)
        if price:
            packages_list = packages_list.filter(price_per_person__lte=price)
        if airport:
            packages_list = packages_list.filter(airport__icontains=airport)

    context = {
        "packages_list" : packages_list,
        "hot_deals" : hot_deals,
    }

    return render(request, "website/packages.html", context)

def flight(request):
    flights_list = Flight.objects.filter(is_active=True).order_by("-price","-id")


    #--------------------- Flights Filter ---------------------------#
    origin = request.GET.get("origin")
    destination = request.GET.get("destination")
    strt_date = request.GET.get("start")
    return_date = request.GET.get("return")
    passengers = request.GET.get("passengers")
    price = request.GET.get("price")
    if origin:
        flights_list = flights_list.filter(origin__icontains=origin)
    if destination:
        flights_list = flights_list.filter(destination__icontains=destination)
    if strt_date:
        flights_list = flights_list.filter(departure_date__gte=strt_date)
    if return_date:
        flights_list = flights_list.filter(return_date__lte=return_date)
    if passengers:
        flights_list = flights_list.filter(available_seats__lte=passengers)
    if price:
        flights_list = flights_list.filter(price__lte=price)

    context = {
        "flights_list" : flights_list,
    }

    return render(request, "website/flight.html", context)