from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.price}"

class Order(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    number = models.IntegerField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default="не подтвержден")


    def __str__(self):
        return f"{self.firstname} {self.lastname}"