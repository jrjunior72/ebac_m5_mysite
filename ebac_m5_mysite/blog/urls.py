from django.urls import path, include

from blog import views


urlpatterns = [
    path("home/", views.PostView.as_view(), name="home"),
    path("post/", views.PostView.as_view(), name="post"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
