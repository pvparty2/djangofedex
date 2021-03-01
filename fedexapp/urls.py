from django.urls import path
from . import views

app_name = 'fedexapp'
urlpatterns = [
    path('', views.ship, name="ship"),
]
