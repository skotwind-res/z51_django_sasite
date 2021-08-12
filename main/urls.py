from django.urls import path
from .views import about, main, contacts, by_rubric, my_apipi

urlpatterns = [
    path('home/', main),
    path('about/', about),
    path('contacts/', contacts),
    path('api/', my_apipi),
    path('home/<int:rubric_id>/', by_rubric),
]