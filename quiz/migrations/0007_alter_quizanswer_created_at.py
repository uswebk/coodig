# Generated by Django 4.1.7 on 2023-08-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_quizanswerchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizanswer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]