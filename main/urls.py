from django.urls import path
from .views import contact, home, about, portifolya





urlpatterns = [
    path('', home, name="home"), 
    path('about/', about, name="about"),
    path('portifolio/', portifolya, name="port"),
    path('contact', contact, name= "contact")
]