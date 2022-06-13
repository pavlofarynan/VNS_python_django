from django.db import models

# Create your models here.


class Forum(models.Model):
    title = models.CharField('Name', max_length=30)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Post')
    date = models.DateTimeField('Date of publish')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/forum/{self.id}'

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
