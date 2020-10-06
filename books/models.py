import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

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

class Review(models.Model):
  book = models.ForeignKey(
    Book,
    on_delete=models.CASCADE,
    related_name="reviews"
  )
  review = models.TextField(max_length=100)
  author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )
  def __str__(self):
    return self.review