from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

#the url path says '<int:pk>/' meaning a variable called pk will be passed to the view, and this variable is an integer.
#looks like it is best to include a / at the end of the url path.
