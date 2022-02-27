from django.db import models
from ckeditor.fields import RichTextField

DEFAULT_STATUS = "draft"

STATUS = [
    # * sol taraf db yazan ismi, sağ taraf UI da görünün ismi
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]

# Create your page models here.


class Page(models.Model):
    title = models.CharField(max_length=200,verbose_name="Başlık")
    slug = models.SlugField(
        max_length=200,
        default="",
        )
    content = models.TextField(verbose_name="İçerik")
    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
        )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
        verbose_name="Durum"
    )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return self.title



class Carousel(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Başlık",
    )
    status = models.CharField(
        default = DEFAULT_STATUS,
        choices = STATUS,
        max_length = 10,
        verbose_name="Durum",
    )
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return self.title


