from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("account/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("logout/", views.logout_request, name="logout"),
    path('post/<pk>', views.post, name='post'),
    path("create", views.PostCreate.as_view(), name="postcreate"),
    path("post/update/<pk>", views.PostUpdate.as_view(), name="postupdate"),
    path("post/delete/<pk>", views.PostDelete.as_view(), name="postdelete")
]