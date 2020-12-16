from django.contrib import admin
from django.urls import path
from Forms import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('Formulario', views.create_form),
    path('login', views.logar),
    path('login/submit', views.submit_logar),
]
