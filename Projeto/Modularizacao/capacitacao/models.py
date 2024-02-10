from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length = 250)
    subtitulo = models.CharField(max_length = 100)

    def __str__(self):
        return self.titulo

