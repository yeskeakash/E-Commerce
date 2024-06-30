from django.urls import path , include
from .views import login_page, register_page


urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
]
