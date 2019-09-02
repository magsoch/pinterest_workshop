from django.db import models

from django.contrib.auth.models import User
class Photo(models.Model):
    file = models.ImageField(upload_to='photos')
    creation_date = models.DateTimeField(
        auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

LIKE_CHOICES = (
    ('thumb', 'Kciuk'),
    ('heart', 'Serce'),
    ('kiss', 'Buziak'),
)

class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE
    )
    type = models.CharField(
        choices=LIKE_CHOICES,
        max_length=10
    )
    class Meta:
        unique_together = (
            ('photo', 'user')
        )