from django.db import models
from main.models import CustomUser as user
# Create your models here.


def images_directory_path(instance, filename):
    return 'series/{0}/{1}'.format(instance.name, filename)


class admin(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'tabel_admin'


class test_upload(models.Model):
    name = models.CharField(max_length=255, default='as')
    image1 = models.ImageField(upload_to=images_directory_path)
    image2 = models.ImageField(upload_to=images_directory_path)
    image3 = models.ImageField(upload_to=images_directory_path)
