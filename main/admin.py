from django.contrib import admin
from .models import SeriesModel, HeroineModel, CustomUser, Voted
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(SeriesModel)
admin.site.register(HeroineModel)
admin.site.register(Voted)