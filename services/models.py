from django.db import models


# Create your models here.


class Service(models.Model):
    # Russian
    service_ru = models.CharField(max_length=120,
                                  verbose_name="Название услуги (РУС)",
                                  null=False, blank=False,
                                  default=None)

    description_ru = models.TextField(default=None,
                                      verbose_name="Краткое описание услуги (РУС)",
                                      null=False, blank=False)

    long_description_ru = models.TextField(default=None,
                                           verbose_name="Полное описание услуги (РУС)",
                                           null=False, blank=False)

    # Uzbek
    service_uz = models.CharField(max_length=120,
                                  verbose_name="Название услуги (UZ)",
                                  null=False, blank=False,
                                  default=None)

    description_uz = models.TextField(default=None,
                                      verbose_name="Краткое описание услуги (УЗ)",
                                      null=False, blank=False)

    long_description_uz = models.TextField(default=None,
                                           verbose_name="Полное описание услуги (УЗ)",
                                           null=False, blank=False)

    # English
    service_en = models.CharField(max_length=120,
                                  verbose_name="Название услуги (АНГ)",
                                  null=False, blank=False,
                                  default=None)

    description_en = models.TextField(default=None,
                                      verbose_name="Краткое описание услуги (АНГ)",
                                      null=False, blank=False)

    long_description_en = models.TextField(default=None,
                                           verbose_name="Полное описание услуги (АНГ)",
                                           null=False, blank=False)

    # Image
    image1 = models.ImageField(default=None, upload_to='img/services/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото1")
    image2 = models.ImageField(default=None, upload_to='img/services/%Y%m%d/',
                               blank=False, null=False,
                               verbose_name="Фото2")

    def __str__(self):
        return self.service_ru

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


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
