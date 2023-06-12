from django.db import models


class Visitors(models.Model):
    name = models.CharField('Имя', max_length=10)
    gender = models.CharField('Пол', max_length=7)
    date = models.DateTimeField('Дата и время входа', max_length=10)
    online = models.BooleanField('Онлайн', max_length=5)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Orders(models.Model):
    visitorNumber = models.ForeignKey(Visitors, on_delete=models.CASCADE)
    title = models.CharField('Категория перевода', max_length=25)
    price = models.IntegerField('Сумма перевода')
    date = models.DateTimeField('Дата и время перевода', max_length=19)

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'