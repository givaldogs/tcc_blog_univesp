from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form, contato, sobre_bellas_unhas

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/',post_detail, name='post_detail'),
    path('save-form/',save_form, name='save_form'),
    path('contato/',contato, name='contato'),
    path('sobre/',sobre_bellas_unhas,name='sobre'),

]
