from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Заголовко', max_length=400)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name=u"Дата создания")
    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True, verbose_name=u"Дата публикации")


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Tik(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Заголовко',max_length=400)
    text = models.TextField(u'Текст')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name=u"Дата создания")
    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True, verbose_name=u"Дата публикации")
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Dubrovka(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Имя файла',max_length=400)
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name=u"Дата создания")
    media_file = models.FileField(upload_to='user_media', verbose_name=u"Загрузить файл")
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
