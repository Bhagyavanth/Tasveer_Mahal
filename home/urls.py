from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:cid>/',views.category1,name='category'),
    path('aboutUs',views.aboutUs,name='About Us'),
    path('search',views.search,name='Search'),
    path('contactUs',views.contact,name='contact us'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

