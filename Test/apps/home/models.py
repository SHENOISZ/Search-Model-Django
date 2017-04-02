from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Home(models.Model):

    nome = models.CharField(max_length=100)
    texto = models.TextField()
    slug = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.nome)
        super(Home, self).save(args, kwargs)