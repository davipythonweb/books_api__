from django.db import models
from books.models import Book


STARS_FOR_REVIEW = (
    ('1', '★'),
    ('2', '★★'),
    ('3', '★★★'),
    ('4', '★★★★'),
    ('5', '★★★★★'),
)

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='reviews'
    )

    stars = models.CharField(
        max_length=10,
        choices=STARS_FOR_REVIEW,
        blank=True,
        null=True,
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.comment