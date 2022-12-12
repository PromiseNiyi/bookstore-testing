from django.urls import path
from . import views
from .views import home
from django.views.generic import TemplateView

urlpatterns = [
    path ('', views.home, name='home'),
    path ('home/', views.home, name ='home'),
    path ('categories/', views.cate, name = 'cate'),
    path ('about/', views.about, name = 'about'),
    path ('blog/', views.blog, name = 'blog'),
    path ('contact/', views.contact, name = 'contact'),
   
    
    path ('home/home.html', views.home, name ='home'),
    path ('home/cate.html', views.cate, name ='cate'),
    path ('home/about.html', views.about, name ='about'),
    path ('home/blog.html', views.blog, name ='blog'),
    path ('home/contact.html', views.contact, name ='contact'),
 



]

