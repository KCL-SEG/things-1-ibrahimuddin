from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,MaxLengthValidator


class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.TextField(
        max_length=120,
        unique=False,
        blank=True,
        validators=[MaxLengthValidator(limit_value=120, message="Description must not have more than 120 characters")]
    )
    quantity = models.IntegerField(unique=False, validators =[
        MinValueValidator(0,message="Quantity must be greater than or equal to 0"),
        MaxValueValidator(100,message="Quantity must be less than or equal to 100")
    ])
    ##

