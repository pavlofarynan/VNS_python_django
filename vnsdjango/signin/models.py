from django.db import models

# Create your models here.


class SignIn(models.Model):
    name = models.CharField('Name', max_length=30)
    surname = models.CharField('Surname', max_length=30)
    mail = models.CharField('E-Mail', max_length=50)
    password = models.CharField('Password', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
