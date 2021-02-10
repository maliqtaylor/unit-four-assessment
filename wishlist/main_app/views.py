from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Wishlist

# Create your views here.
def home(request):
  wishlist = Wishlist.objects.all()
  return render(request, 'wishlist.html',{'wishlist': wishlist})

class ItemCreate(CreateView):
  model = Wishlist
  fields= '__all__'
  success_url = '/'

class ItemDelete(DeleteView):
  model = Wishlist
  success_url = '/'
