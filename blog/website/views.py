from django.shortcuts import render
from .models import Post, Contact

# Create your views here.

def hello_blog(request):
      list = [
            'Django', 'Python', 'Git', 'Html', 
            'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi',
            'Systemclt'
      ]
      list_posts = Post.objects.filter(deleted=False)
      data ={'name': 'Curso de Django 3', 'lista_tecnologias':list,
             'posts': list_posts
             }
      return render(request, 'index.html', data)

    
def post_detail(request, id):
      post = Post.objects.get(id=id)
      return render(request, 'post_detail.html',{'post': post})

def save_form(request):
      name=request.POST['name']
      Contact.objects.create(
            name=name,
            email=request.POST['email'],
            message=request.POST['message']
      )
      return render(request, 'contact_success.html', {'name_contact': name})

def contato(request):
      return render(request, 'contato.html')

def sobre_bellas_unhas(request):
      return render(request, 'sobre_bellas_unhas.html')

