from django.contrib import admin
from django.urls import path, include
from account.views import *

app_name ='account'
urlpatterns = [
    path('login/', login_view,name="login"),
    path('signup/', register_view,name="signup"),
    path('forget/', forget_view,name="forget"),
    path('logout/', logout_view,name="logout"),
    path("admin/", admin.site.urls),
]

