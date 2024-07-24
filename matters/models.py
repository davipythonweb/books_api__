from django.db import models


class Matter(models.Model):
    matter = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.matter
