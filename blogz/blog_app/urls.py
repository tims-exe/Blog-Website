from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add', views.add_blog, name='add'),
    path('save', views.save_blog, name='save'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete'),
    path('update/<int:blog_id>/', views.get_blog_info, name='getbloginfo'),
    path('updateblog/<int:blog_id>/', views.update_blog, name="update"),
    #path('test', views.test_function, name="test")
]
