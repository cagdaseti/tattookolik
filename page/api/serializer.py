from rest_framework import serializers
from page.models import Page,Carousel


class PageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    slug = serializers.SlugField()
    content = serializers.CharField()
    cover_image = serializers.ImageField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        print(validated_data)
        return Page.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.content = validated_data.get('content',instance.content)
        instance.cover_image = validated_data.get('cover_image',instance.cover_image)
        instance.status = validated_data.get('status',instance.status)
        instance.save()


class CarouselSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    status = serializers.CharField()
    cover_image = serializers.ImageField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        print(validated_data)
        return Carousel.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.status = validated_data.get('status',instance.status)
        instance.cover_image = validated_data.get('cover_image',instance.cover_image)
        instance.save()
