from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100) # задаем ограничение для заголовка
    description = models.CharField(max_length=250) # задаем ограничение для описания
    image = models.ImageField(upload_to='portfolio/images/') # upload_to в какой папке сохраняются изображения
    url = models.URLField(blank=True) # так как элементы будут кликабельну и вести куда то (blank=открывать в новой вкладке или нет)

    def __str__(self):
        return self.title   