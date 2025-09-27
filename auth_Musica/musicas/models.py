from django.db import models

# Create your models here.

    # CHOICES de raridade
GENERO_CHOICES = [
    ('BRC', "BREAKCORE"),
    ('POP', "POP"),
    ('JPOP', "J-POP"),
    ('RCK', "ROCK"),
    ('JRCK', "J-ROCK"),
    ('MTL', "METAL"),
    ('JMTL', "J-METAL"),
    ('RAP', "RAP"),
    ('JRAP', "J-RAP"),
    ('CLSC', "Classica"),
    ('MPB', "Musica Popular Brasileira"),
    ]

class Musicas(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    artist = models.CharField(max_length=100, verbose_name='Artista')
    album = models.CharField(max_length=100, verbose_name='Album')
    genre = models.CharField(max_length=100, verbose_name='Genero', choices=GENERO_CHOICES)
    releaseDate = models.DateField()

    class Meta:
        verbose_name = 'Musica'
        verbose_name_plural = 'Musicas'
    def __str__(self):
        return self.name