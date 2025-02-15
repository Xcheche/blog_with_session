from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.post_page, name='post_page'),
]