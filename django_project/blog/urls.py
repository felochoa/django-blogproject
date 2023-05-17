from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name= "home"),
    
         
]

""" All blog post entries will start with post/. Next is the primary key for our post entry which will
be represented as an integer, <int:pk> """