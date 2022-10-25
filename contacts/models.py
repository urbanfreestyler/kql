from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Email(models.Model):
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Phone(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Номера телефонов'
        verbose_name_plural = 'Номера телефонов'

class Address(models.Model):
    address_ru = models.CharField(max_length=50, verbose_name="Адрес (РУС)",
                                  default=None,
                                  blank=False,
                                  null=False)
    address_uz = models.CharField(max_length=50, verbose_name="Адрес (УЗБ)",
                                  default=None,
                                  blank=False,
                                  null=False)
    address_en = models.CharField(max_length=50, verbose_name="Адрес (АНГ)",
                                  default=None,
                                  blank=False,
                                  null=False)


    def __str__(self):
        return self.address_ru

    class Meta:
        verbose_name = 'Адреса'
        verbose_name_plural = 'Адреса'


class SocialMedia(models.Model):
    icon = models.FileField(validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg'])],
                            verbose_name="Иконка соц. сети",
                             help_text="Эта иконка будет отображаться на сайте. Нажав на эту иконку, пользователь"
                                       " будет отправлен по ссылке.",
                             upload_to='icons/%Y%m%d/',
                             default=None)
    link = models.CharField(max_length=50, verbose_name='Ссылка',
                            help_text="Вставьте полную ссылку. Например 'https://www.instagram.com/instagram/'")

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Соц. соти'
        verbose_name_plural = 'Соц. соти'


class MetaTag(models.Model):

    metatag = models.TextField(null=False, blank=False,
                              verbose_name="Keywords (Через запятую / предложением",
                              help_text="Введите ключевые слова через запятую / Предложением",
                               default=None)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "Мета-теги"
        verbose_name_plural = "Мета-теги"
