from django.shortcuts import render,redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm




class SinUp(View):

        
    def get(self, request):
        form = UserForm()
        return render(request, 'accounts/signup.html' , {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('home')

        return render(request, 'accounts/signup.html', {'form':form})
  
def home(request):
    return render(request, 'home.html')
# Create your views here.
