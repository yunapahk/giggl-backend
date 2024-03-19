from django.urls import path
from .views import SignupView, profile_view
from django.contrib.auth import views as accounts_views

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', accounts_views.LoginView.as_view(), name='login'),
    path('logout/', accounts_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile')
]
