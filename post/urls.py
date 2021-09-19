from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<pk>', views.post, name='post'),
    path("create", views.PostCreate.as_view(), name="postcreate"),
    path("post/update/<pk>", views.PostUpdate.as_view(), name="postupdate"),
    path("post/delete/<pk>", views.PostDelete.as_view(), name="postdelete")
]