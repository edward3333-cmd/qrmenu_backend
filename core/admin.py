from django.contrib import admin
from . import models

admin.site.site_header = "UTAS Admin"
# Register your models here.
admin.site.register(models.Places)
admin.site.register(models.Category)
admin.site.register(models.MenuItem)