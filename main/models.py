from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_voters = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    object = CustomUserManager()

    def __str__(self):
        return self.email


class SeriesModel(models.Model):
    kode = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    gambar_header = models.CharField(max_length=255)
    gambar_body = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class HeroineModel(models.Model):
    kode = models.AutoField(primary_key=True)
    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)
    voice_actor = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.nama

class Voted(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    series = models.ForeignKey(SeriesModel, on_delete = models.CASCADE)
    choice = models.CharField(max_length = 255)