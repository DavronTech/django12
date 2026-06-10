from django.urls import path
from .views import SinUp,LoginView,logout_view, ProfilView

urlpatterns = [
    path('sign-up/', SinUp.as_view(), name='sign_up'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfilView.as_view(), name='profile'),
]