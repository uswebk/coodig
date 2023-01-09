# Generated by Django 4.1.4 on 2023-01-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiztag_quiz_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('is_answer', models.BooleanField(default=False)),
                ('sort', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.quiz')),
            ],
            options={
                'db_table': 'quiz_choices',
            },
        ),
    ]
