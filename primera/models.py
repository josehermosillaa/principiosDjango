from django.db import models

# Create your models here.
TITLE_CHOICES = [
    ('MR','Mr.'),
    ('MRS','Mrs.'),
    ('MS','Ms.'),
]
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("es_miembro_1", "Es miembro con prioridad 1"),
            )
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['-created']


    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created']