from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('sign-up',views.sign_up, name='sign_up'),
    path('create-post', login_required(views.PostCreation.as_view()), name='create_post'),

]