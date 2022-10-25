from django.db import models


# Create your models here.

class Team(models.Model):
    name_ru = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            default=None,
                            verbose_name="Имя и фамилия (РУС)")

    position_ru = models.CharField(max_length=30,
                                blank=False,
                                null=False,
                                default=None,
                                verbose_name="Должность (РУС)")

    name_uz = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            default=None,
                            verbose_name="Имя и фамилия (УЗБ)")

    position_uz = models.CharField(max_length=30,
                                blank=False,
                                null=False,
                                default=None,
                                verbose_name="Должность (УЗБ)")

    name_en = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            default=None,
                            verbose_name="Имя и фамилия (АНГ)")

    position_en = models.CharField(max_length=30,
                                blank=False,
                                null=False,
                                default=None,
                                verbose_name="Должность (АНГ)")





    image = models.ImageField(default=None,
                              blank=False,
                              null=False,
                              verbose_name="Фото",
                              upload_to="img/about/team/%Y%m%d/")

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команда"


class AboutUs(models.Model):
    header_ru = models.CharField(max_length=50,
                                 null=False,
                                 blank=False,
                                 verbose_name="Заголовок (РУС)",
                                 default=None)

    text_ru = models.TextField(verbose_name="Текст (РУС)",
                               default=None,
                               blank=False,
                               null=False)

    header_uz = models.CharField(max_length=50,
                                 null=False,
                                 blank=False,
                                 verbose_name="Заголовок (УЗБ)",
                                 default=None)

    text_uz = models.TextField(verbose_name="Текст (УЗБ)",
                               default=None,
                               blank=False,
                               null=False)

    header_en = models.CharField(max_length=50,
                                 null=False,
                                 blank=False,
                                 verbose_name="Заголовок (АНГ)",
                                 default=None)

    text_en = models.TextField(verbose_name="Текст (АНГ)",
                               default=None,
                               blank=False,
                               null=False)

    image = models.ImageField(default=None,
                              blank=False,
                              null=False,
                              verbose_name="Картинка",
                              upload_to="img/about/%Y%m%d/")

    image_webp = models.ImageField(default=None,
                                   blank=False,
                                   null=False,
                                   verbose_name="Картинка",
                                   upload_to="img/about/%Y%m%d/",
                                   help_text="Важно! Загрузите картинку в формате .webp")

    class Meta:
        verbose_name = "Описание"
        verbose_name_plural = "Описание"

    def __str__(self):
        return self.header_ru


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
