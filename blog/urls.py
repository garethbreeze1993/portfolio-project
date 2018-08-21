from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.all_posts, name='blog_home'),	
    path('<int:blog_id>/',views.detail, name='detail'), # looks for a number after our /blog on our site.
    	
] 