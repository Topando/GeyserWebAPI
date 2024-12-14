from django.db import models
from django.utils.text import slugify


class Journal(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.SlugField(max_length=150, unique=True, blank=True, verbose_name="Символьный код")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    announcement = models.TextField(null=True, blank=True, verbose_name="Анонс")
    description = models.TextField(verbose_name="Описание")
    order = models.PositiveSmallIntegerField(default=1, verbose_name="Сортировка")
    photo_detail = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True, verbose_name="Детальное фото")
    photo_announcement = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True, verbose_name="Фото анонса")
    beginning_activity = models.DateField(null=True, blank=True, verbose_name="Начало активности")
    seo_title = models.TextField(blank=True, verbose_name="SEO TITLE")
    seo_description = models.TextField(null=True, blank=True, verbose_name="SEO DESCRIPTION")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = "Журнал"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.seo_title:
            self.seo_title = self.title + " | ГЕЙЗЕР"
        if not self.seo_description:
            self.seo_description = self.description + " - ознакомиться с содержанием | ГЕЙЗЕР"
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title