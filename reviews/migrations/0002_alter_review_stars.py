# Generated by Django 5.0.7 on 2024-07-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(blank=True, choices=[('one', '★'), ('two', '★★'), ('three', '★★★'), ('four', '★★★★'), ('five', '★★★★★')], max_length=10, null=True),
        ),
    ]
