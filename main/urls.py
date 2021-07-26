from django.urls import path
from .views import about, main, contacts

urlpatterns = [
    path('home/', main),
    path('about/', about),
    path('contacts/', contacts)
]