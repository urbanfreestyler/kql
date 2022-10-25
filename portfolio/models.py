from django.db import models

# Create your models here.


class Portfolio(models.Model):

    header_ru = models.CharField(max_length=120, verbose_name="Заголовок", blank=False, null=False)
    header_uz = models.CharField(max_length=120, verbose_name="Заголовок (УЗБ)", blank=False, null=False)
    header_en = models.CharField(max_length=120, verbose_name="Заголовок (АНГ)", blank=False, null=False)

    image1 = models.ImageField(default=None,
                               upload_to='img/portfolio/%Y%m%d/',
                              blank=False, null=False,
                              verbose_name="Фото1")

    image2 = models.ImageField(default=None,
                               upload_to='img/portfolio/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото2")

    image3 = models.ImageField(default=None,
                               upload_to='img/portfolio/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото3")

    image4 = models.ImageField(default=None,
                               upload_to='img/portfolio/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото4")

    image5 = models.ImageField(default=None,
                               upload_to='img/portfolio/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото5")

    def __str__(self):
        return self.header_ru

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"


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


