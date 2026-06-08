from django.urls import path
from .views import SinUp

urlpatterns = [
    path('sign-up/', SinUp.as_view(), name='sign_up'),
]