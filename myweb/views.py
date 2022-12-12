from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse('hello world')
   return render(request, 'home.html')

def cate(request):
   # return HttpResponse('hello world')
   return render(request, 'cate.html')

def about(request):
   # return HttpResponse('hello world')
   return render(request, 'about.html')

def blog(request):
   # return HttpResponse('hello world')
   return render(request, 'blog.html')

def contact(request):
   # return HttpResponse('hello world')
   return render(request, 'contact.html')
