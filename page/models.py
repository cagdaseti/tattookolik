from django.db import models

DEFAULT_STATUS = "draft"

STATUS = [
    # * sol taraf db yazan ismi, sağ taraf UI da görünün ismi
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]

# Create your page models here.


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
        )
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
        )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    status = models.CharField(
        default = DEFAULT_STATUS,
        choices = STATUS,
        max_length = 10,
    )
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


