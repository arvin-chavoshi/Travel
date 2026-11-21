from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'website'

urlpatterns = [
    path("index/", views.index ,  name="index"),
    path("contact/", views.contact , name="contact"),
    path("about/", views.about, name="about"),
    path("elements/", views.elements , name="elements"),
    path("destination/<int:pk>/", views.destination_details, name="destination_details"),
    path("hotels/", views.hotels, name="hotels"),
    path("packages/", views.packages, name="packages"),
    path("insurance/", views.insurance, name="insurance"),
    path("flight/", views.flight, name="flight"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)