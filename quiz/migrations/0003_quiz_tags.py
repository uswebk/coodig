# Generated by Django 4.1.4 on 2023-01-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='quiz.tag'),
        ),
    ]
