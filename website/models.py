from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='destination/images')
    description = models.TextField()

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/hotels", blank=True, null=True)
    reviews = models.PositiveIntegerField(default=0)
    rating = models.PositiveSmallIntegerField()
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    room_service = models.BooleanField(default=False)
    air_condition = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    price_pernight = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/packages", blank=True, null=True)
    country = models.CharField(max_length=200)
    days = models.PositiveSmallIntegerField()
    nights = models.PositiveSmallIntegerField()
    date = models.DateField(blank=True, null=True)
    airport = models.CharField(max_length=200)
    extras = models.CharField(max_length=200)
    price_per_person = models.DecimalField(max_digits=8, decimal_places=2)
    is_hot_deal = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    PACKAGE_TYPE = [
        ("cheap", "Cheap"),
        ("luxury", "Luxury"),
        ("camping", "Camping"),
    ]
    package_type = models.CharField(
        max_length=20,
        choices=PACKAGE_TYPE,
        default="cheap",
    )

    def __str__(self):
        return self.title

class Flight(models.Model):
    airline = models.CharField(max_length=200)
    flight_number = models.CharField(max_length=200, unique=True)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_seats = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"origin : {self.origin} , destination : {self.destination}"

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/users", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name