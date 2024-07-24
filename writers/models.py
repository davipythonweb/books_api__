from django.db import models

NATIONALITY_CHOICES =(
    ('USA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
    ('FRA', 'França'),
    ('COL', 'Colombia'),
    ('CHN', 'China'),
    ('JPN', 'Japão'),
    ('NLD', 'Holanda'),
    ('GRC', 'Grecia')

)

class Writer(models.Model):
    writer = models.CharField(max_length=40)
    nationality = models.CharField(
        max_length=20,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.writer
