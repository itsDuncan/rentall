from django.db import models
from django.utils.text import slugify
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Property(models.Model):
	slug = models.SlugField(
		unique=True,
		blank=True,
		null=True
	)

	name = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	address = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	image = models.ImageField(
		upload_to='properties',
		blank=True,
		null=True
	)

	rent = models.IntegerField()
	description = models.TextField()
	bedrooms = models.IntegerField()
	washrooms = models.IntegerField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

class Appartment(models.Model):
	slug = models.SlugField(
		unique=True,
		blank=True,
		null=True
	)

	name = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	location = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


class House(models.Model):
	slug = models.SlugField(
		unique=True,
		blank=True,
		null=True
	)

	name = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	address = models.CharField(
		max_length=50,
		blank=True,
		null=True
	)

	vacant = models.BooleanField(default=True)

	appartment = models.ForeignKey(
		Appartment,
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)

	tenant = models.ForeignKey(
		User,
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)

	rent = models.IntegerField()
	description = models.TextField()
	bedrooms = models.IntegerField()
	washrooms = models.IntegerField()

	@property
	def is_vacant(self):
		return self.vacant

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('properties:properties-detail', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

class OccupiedHouse(models.Model):
	house = models.OneToOneField(
		House,
		on_delete=models.CASCADE,
		null=True,
		related_name='occupied_house'
	)

	rent_status = models.CharField(
		max_length=15,
		blank=True,
		null=True,
		default='PENDING'
	)

	def __str__(self):
		return self.house.name

@receiver(post_save, sender=House)
def house_postsave(sender, instance, created, *args, **kwargs):
	if instance.is_vacant == False:
		OccupiedHouse.objects.get_or_create(house=instance)