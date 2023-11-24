from django.urls import path
from .views import homepage, login_user, logout_user


app_name='shop'
urlpatterns = [
    path('', homepage, name='home'),
    path('login/', login_user,name='login'),
    path('logout/', logout_user,name='logout'),
   # path('signup/', signup_user,name='singup'),
]