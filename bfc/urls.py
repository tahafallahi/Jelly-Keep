from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('', include('word.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=LoginForm)),
    path('accounts/', include('django.contrib.auth.urls')), 
    ]
