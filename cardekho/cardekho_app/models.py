from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
class showroomlist(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 20)
    website = models.URLField(max_length = 30)

    def __str__(self):
        return self.name


class carlist(models.Model):
    model = models.CharField(max_length = 20)
    description = models.CharField(max_length = 50)
    Active = models.BooleanField(default = False)
    chassisnumber = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null = True)
    showroom = models.ForeignKey(showroomlist, on_delete = models.CASCADE, related_name= "cars", null = True)

    def __str__(self):
        return self.model


class review(models.Model):
    rating = models.IntegerField(validators = [MaxLengthValidator, MinLengthValidator])
    comments = models.CharField(max_length = 100, null = True)
    cars = models.ForeignKey(carlist, on_delete = models.CASCADE, related_name = "reviews", null = True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "The Rating of " + " " + self.cars.model + " " + "is" + " " + str(self.rating)

