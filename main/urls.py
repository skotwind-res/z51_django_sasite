from django.urls import path
from .views import about, main, contacts, by_rubric
urlpatterns = [
    path('home/', main),
    path('about/', about),
    path('contacts/', contacts),
    path('home/<int:rubric_id>/', by_rubric),
]