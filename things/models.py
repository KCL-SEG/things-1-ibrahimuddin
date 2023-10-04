from django.db import models
from django.core.validators import RegexValidator

class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.TextField(unique=False, max_length=120)
    quantity = models.IntegerField(
        unique=False,
        validators=[
            RegexValidator(
                regex=r"^(100|[1-9]?[0-9])$",
                message="must be a value between 0 and 100",
                ),
                ], 
                )
    

