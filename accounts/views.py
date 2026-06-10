from django.shortcuts import render,redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError




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

            return redirect('login')

        return render(request, 'accounts/signup.html', {'form':form})
  
def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
       
        return render(request, 'accounts/login.html', {'form': form})
        
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get('username')
            password =  form.cleaned_data.get('password')
            user = authenticate(
    username=username,
    password=password
)

            print("USER =", user)
     
            print("USER =", user)


            user = authenticate(username = username, password = password)

            if not  user:
                raise ValidationError('Username yoki parol notogri ')
            

            login(request, user )

            return redirect( 'home')
        
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

class ProfilView(View):

    def get(self , request):
        return render(request , 'accounts/profile.html' )