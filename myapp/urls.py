from django.urls import path

from myapp.views import create_blog

urlpatterns=[
    path('', create_blog,name="blog_create"),
]