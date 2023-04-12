from django.db import models

# Create your models here.
class Customer(models.Model):
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    addres = models.CharField(max_length=255, verbose_name="Адрес")
    facs_number = models.IntegerField()

    def __str__(self):
        return self.surname