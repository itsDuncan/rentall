from django.db import models
from django.utils.text import slugify

class Property(models.Model):
	slug = models.SlugField(unique=True, blank=True, null=True)
	name = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(upload_to='properties', blank=True, null=True)
	rent = models.IntegerField()
	description = models.TextField()
	bedrooms = models.IntegerField()
	washrooms = models.IntegerField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)