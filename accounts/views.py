from django.shortcuts import render,redirect
from django.views import View
from .models import CustomUser
from .forms import UserForm,LoginForm,UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import send_test_email,send_email_login




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
            send_test_email(user.email)


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
            send_email_login(user.email)

            return redirect( 'home')
        
        return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

class ProfilView(View):

    def get(self , request):
        return render(request , 'accounts/profile.html' )


class UserUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, 'accounts/update.html', {'form': form})

    def post(self, request):
        form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

        return render(request, 'accounts/update.html', {'form': form})