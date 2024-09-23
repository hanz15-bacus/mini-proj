from django.urls import path
from. import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('register/',views.register_view,name='register'),
    path('post_list/',views.post_list,name='post_list'),

    
]
