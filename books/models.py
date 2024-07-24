from django.db import models

from matters.models import Matter
from knowledge_area.models import Knowledge_Area
from writers.models import Writer


class Book(models.Model):
    title = models.CharField(max_length=30)
    publishing_company = models.CharField(max_length=30, default="")
    knowledge_area = models.ForeignKey(
        Knowledge_Area,
        on_delete=models.PROTECT,
        related_name='books'
    )
    release_date = models.DateField(
        null=True,
        blank=True
    )
    matter = models.ManyToManyField(
        Matter,
        related_name='books'
    )
    writer = models.ForeignKey(
        Writer,
        default="",
        on_delete=models.PROTECT,
        related_name='books'
    )
    resume = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title