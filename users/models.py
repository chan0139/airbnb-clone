
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):  # AbstractUser class 상속
    """ Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES  = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_ENGLISH = "en"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Kr"),
        (LANGUAGE_ENGLISH, "En"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "Usd"),
        (CURRENCY_KRW, "Krw"),
    )
    
    avatar = models.ImageField(upload_to = "avatars",blank = True) #blank는 form , null 은 DB에 적용
    gender = models.CharField(choices =GENDER_CHOICES,max_length=10, blank = True)
    bio = models.TextField(blank = True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices =LANGUAGE_CHOICES,max_length=10, blank = True)
    currency = models.CharField(choices =CURRENCY_CHOICES,max_length=10, blank = True)
    superhost = models.BooleanField(default=False)