from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):

    CATEGORY = [
        ("Aventura", "Aventura"),
        ("Romance", "Romance"),
        ("Ficção Científica", "Ficção Científica"),
        ("Fantasia", "Fantasia"),
        ("Mistério", "Mistério"),
        ("Policial", "Policial"),
        ("Drama", "Drama"),
        ("Comédia", "Comédia"),
        ("Ação", "Ação"),
        ("História Real", "História Real"),
        ("Autoajuda", "Autoajuda"),
        ("Terror", "Terror"),
        ("Sci-Fi", "Sci-Fi"),
        ("Fantasia Científica", "Fantasia Científica"),
        ("Suspense", "Suspense"),
        ("Histórico", "Histórico"),
        ("Biografia", "Biografia"),
        ("Autobiografia", "Autobiografia"),
        ("Ensino", "Ensino"),
        ("Referência", "Referência"),
        ("Religião", "Religião"),
        ("Espiritualidade", "Espiritualidade"),
        ("Psicologia", "Psicologia"),
        ("Autoconhecimento", "Autoconhecimento"),
        ("Culinária", "Culinária"),
        ("Viagem", "Viagem"),
        ("Hobby", "Hobby"),
        ("Artes", "Artes"),
        ("Ciência", "Ciência"),
        ("História", "História"),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(
        max_length=100, choices=CATEGORY, default='')
    description = models.TextField(null=False, blank=False)
    release_date = models.DateField(default=timezone.now, blank=False)
    user_id = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.name
