from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length= 20,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(100)],
        help_text="Percentage Value"
    )
    active = models.BooleanField()
    def __str__(self):
        return self.code
