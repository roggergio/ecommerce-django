from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=20, unique=True)
    description=models.CharField(max_length=255, blank=True)
    slug =models.CharField(max_length=100, unique=True)
    cat_image=models.ImageField(upload_to='photos/categories', blank=True)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural= 'categories'
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
#una vez que tengas el modelo creado

#registralo en admin admin.site.register(Category)
#no olvides importar from . import tu_modelo_creado
#abre el git e installa pillow
#pip install pillow
#ahora haz la migracion con el comando python manage.py makemigrations
#python manage.py migrations

#crea un superusuario
#en git escribe el comando winpty python manage.py createsuperuser
