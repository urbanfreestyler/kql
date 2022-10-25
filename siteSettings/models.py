from django.db import models

# Create your models here.


class Favicon(models.Model):
    favicon = models.ImageField(verbose_name="Иконка сайта", upload_to='img/%Y%m%d/')

    class Meta:
        verbose_name = "Favicon"
        verbose_name_plural = "Favicon"

    def __str__(self):
        return "Иконка сайта"


class TagForHead(models.Model):
    description = models.CharField(max_length=25, verbose_name="Для чего нужен этот тег?")

    code = models.TextField(verbose_name="HTML-Код, для <head> элемента:")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Тэги для <head>"
        verbose_name_plural = "Тэги для <head>"


class FirstBlock(models.Model):
    header_ru = models.CharField(max_length=120,
                              verbose_name="Заголовок (РУС)",
                              null=False,
                              blank=False)

    text_ru = models.TextField(verbose_name="Текст заголовка (РУС)",
                            null=False,
                            blank=False)

    header_uz = models.CharField(max_length=120,
                              verbose_name="Заголовок (УЗБ)",
                              null=False,
                              blank=False)

    text_uz = models.TextField(verbose_name="Текст заголовка (УЗБ)",
                            null=False,
                            blank=False)

    header_en = models.CharField(max_length=120,
                              verbose_name="Заголовок (АНГ)",
                              null=False,
                              blank=False)

    text_en = models.TextField(verbose_name="Текст заголовка (АНГ)",
                            null=False,
                            blank=False)

    image = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                              blank=False,
                              null=False,
                              verbose_name="Картинка")

    def __str__(self):
        return self.header_ru

    class Meta:
        verbose_name = "Первый блок"
        verbose_name_plural = "Первый блок"


class SecondBlock(models.Model):
    header_ru = models.CharField(max_length=120,
                                 verbose_name="Заголовок (РУС)",
                                 null=False,
                                 blank=False)

    header_uz = models.CharField(max_length=120,
                                verbose_name="Заголовок (УЗБ)",
                                null=False,
                                blank=False)

    header_en = models.CharField(max_length=120,
                                verbose_name="Заголовок (АНГ)",
                                null=False,
                                blank=False)

    image1 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                              blank=False,
                              null=False)
    text1_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text1_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text1_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    image2 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)

    text2_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text2_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text2_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    image3 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                                   blank=False,
                                   null=False)

    text3_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text3_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text3_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    image4 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)

    text4_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text4_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text4_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    image5 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)

    text5_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text5_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text5_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    image6 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)

    text6_ru = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (РУС)", help_text="Текст будет появляться при навдении на картинку")
    text6_uz = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (УЗБ)", help_text="Текст будет появляться при навдении на картинку")
    text6_en = models.CharField(max_length=30,
                                null=False,
                                blank=False,
                                verbose_name="Текст (АНГ)", help_text="Текст будет появляться при навдении на картинку")


    def __str__(self):
        return self.header_ru

    class Meta:
        verbose_name = "Второй блок"
        verbose_name_plural = "Второй блок"


class ThirdBlock(models.Model):
    header_ru = models.CharField(max_length=120,
                                 verbose_name="Заголовок (РУС)",
                                 null=False,
                                 blank=False)

    header_uz = models.CharField(max_length=120,
                                verbose_name="Заголовок (УЗБ)",
                                null=False,
                                blank=False)

    header_en = models.CharField(max_length=120,
                                verbose_name="Заголовок (АНГ)",
                                null=False,
                                blank=False)

    image1 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image2 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image3 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image4 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image5 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image6 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image7 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)
    image8 = models.ImageField(upload_to="img/mainpage/%Y%m%d/",
                               blank=False,
                               null=False)

    def __str__(self):
        return self.header_ru

    class Meta:
        verbose_name = "Третий блок"
        verbose_name_plural = "Третий блок"