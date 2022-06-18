from django.urls import path
from .views import xyz_hotel, fetch_guest, Signup, login_view, logout_view, home 

app_name = "home"


urlpatterns = [
    path("", home, name="home"),
    path("xyz hotel/", xyz_hotel, name="xyz hotel"),
    path("fetch_guest/", fetch, name="fetch"),
    path("register/", Signup, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]