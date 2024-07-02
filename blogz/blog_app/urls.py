from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test', views.test_function, name="test")
]
