from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Заголовок', max_length=400)
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

class Pogar(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Заголовок', max_length=400)
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

class Sevsk(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Заголовок', max_length=400)
    text = models.TextField(u'Описание')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name=u"Дата создания")
    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True, verbose_name=u"Дата публикации")


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Calendar(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=u"Пользователь")
    title = models.CharField(u'Название', max_length=400)
    text = models.TextField(u'Описание')

    published_date = models.DateTimeField(default=timezone.now,
            blank=True, null=True, verbose_name=u"Дата события")


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
