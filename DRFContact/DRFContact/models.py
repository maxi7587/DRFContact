from django.db import models
from django.utils import timezone

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100) # province
    city = models.CharField(max_length=100)
    street_name = models.CharField(max_length=100)
    street_number = models.IntegerField()
    zip = models.CharField(max_length=15)
    detail = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.street_name

    class Meta:
        ordering = ('id',)

class Phone(models.Model):
    country_code = models.IntegerField()
    area_code = models.IntegerField()
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.phone_number)

    class Meta:
        ordering = ('id',)


class Web(models.Model):
    email = models.CharField(max_length=100, blank=True)
    web_url = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('id',)

class SocialMedia(models.Model):
    web_contact = models.ForeignKey(Web, related_name='social_media', on_delete=models.CASCADE, null=True)
    social_network = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.link

    class Meta:
        ordering = ('id',)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, related_name='contact_address', null=True, on_delete=models.SET_NULL)
    phone = models.ForeignKey(Phone, related_name='contact_phone', null=True, on_delete=models.SET_NULL)
    web = models.ForeignKey(Web, related_name='contact_web', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
