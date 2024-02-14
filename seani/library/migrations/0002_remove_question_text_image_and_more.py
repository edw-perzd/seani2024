# Generated by Django 5.0.2 on 2024-02-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='text_image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text_question',
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions', verbose_name='Imagen de la pregunta'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Texto de la pregunta'),
        ),
    ]
