from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(
        upload_to='image/'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
class Contact(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name='Имя пользовотеля'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    message =  models.TextField(
        verbose_name='Сообщение'
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'    