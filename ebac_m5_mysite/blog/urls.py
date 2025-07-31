from django.contrib import admin
from django.urls import path, include

from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),  # <-- ESSA LINHA É ESSENCIAL
    path("home/", views.PostView.as_view(), name="home"),
    path("post/", views.PostView.as_view(), name="post"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
