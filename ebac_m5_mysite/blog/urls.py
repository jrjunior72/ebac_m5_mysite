from django.urls import path, include

from blog import views


urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    # path('home', include('blog.urls'))
]