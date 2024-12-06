from django.db import models

# Create your models here.
#

class Categories(models.TextChoices):
    TECH = "TC", 'Tecnologia'
    SALAOBLZ  = 'BE', 'Salao Beleza'
    CR = 'CR', 'Curiosidade'
    GR = 'GR', 'Geral'
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title= models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.GR,
    )
    deleted = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title
    
    # def get_category_label(self):
    #     return self.categories
    
    
    full_name.admin_order_field = 'title'