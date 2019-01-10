# Generated by Django 2.1.4 on 2019-01-09 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_dubrovka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dubrovka',
            name='author',
        ),
        migrations.RemoveField(
            model_name='tik',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=400, verbose_name='Заголовок'),
        ),
        migrations.DeleteModel(
            name='Dubrovka',
        ),
        migrations.DeleteModel(
            name='Tik',
        ),
    ]