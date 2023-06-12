from django.db import models


class Visitors(models.Model):
    name = models.CharField('Имя', max_length=10)
    gender = models.CharField('Пол', max_length=7)
    date = models.DateTimeField('Дата и время входа', max_length=10)
    online = models.BooleanField('Онлайн', max_length=5)

    def get_absolute_url(self):
        return '/'

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


class Bank(models.Model):
    name = models.CharField('Название банка', max_length=10)
    address = models.CharField('Месторасположение банка', max_length=25)
    square = models.IntegerField('Рейтинг', max_length=2)

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'


class Employees(models.Model):
    bankId = models.OneToOneField(Bank, on_delete = models.CASCADE, primary_key = False)
    name = models.CharField('Имя', max_length=10)
    gender = models.CharField('Пол', max_length=7)
    position = models.CharField('Должность', max_length=25)
    salary = models.IntegerField('Заработная плата', max_length=6)

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Intermediary(models.Model):
    customerId = models.ManyToManyField(Bank)
    product = models.CharField('Категория перевода', max_length=10)
    time = models.IntegerField('Сроки перевода', max_length=1)
    guarantee = models.BooleanField('Гарантия', max_length=5)

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = 'Посредник'
        verbose_name_plural = 'Посредники'

