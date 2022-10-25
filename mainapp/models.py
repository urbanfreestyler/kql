from django.db import models


# Create your models here.


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


class Application(models.Model):
    name = models.CharField(max_length=30, default=None,
                            blank=False,
                            null=False)
    phone = models.CharField(max_length=25, default=None,
                             blank=False,
                             null=False)
    email = models.EmailField(max_length=50, default=None,
                              blank=False,
                              null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявки"
        verbose_name_plural = "Заявки"
