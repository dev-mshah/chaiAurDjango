from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about',views.about,name='about'),
    path('chai/',include('chai.urls')),
    
    path("__reload__/", include("django_browser_reload.urls"))

]