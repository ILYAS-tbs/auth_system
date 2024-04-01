from django.shortcuts import render
from django.http import HttpResponse

from .forms import MyUserCreationForm
# Create your views here.

def create_user_view(request):

   if (request.method == 'POST'): 
      form = MyUserCreationForm(request.POST)
      print("we got a POST request")
      
      if form.is_valid(): 
         form.save()

      else:
         print(" Form invalid for some reasonn")
   
   else:
      form = MyUserCreationForm()
   
   # return render(request , 'api/register.html', {'form':form})
   return render(request , 'api/after_login.html')
   
      

def second_page_view(request):


   return HttpResponse('linking working fine ')