from django.db import models
import uuid

from django.urls import reverse

class Book(models.Model):
  title = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10,decimal_places=0)
  author = models.CharField(max_length=200)

  id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid1,
    editable=False
  )

  def __str__(self):
    return self.title

  
  def get_absolute_url(self):
    return reverse('book_detail', args=[str(self.id)])