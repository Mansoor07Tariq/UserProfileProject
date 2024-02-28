from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

def validate_phone_number(value):
    if not all(char.isdigit() or char == '+' for char in value):
        raise ValidationError('Phone number must contain only digits.')

class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[validate_phone_number],
        help_text='Enter a phone number with digits.'
    )

    def __str__(self):
        return f"{self.first_name} {self.surname}"