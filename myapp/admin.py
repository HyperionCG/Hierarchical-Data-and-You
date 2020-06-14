from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from myapp.models import Car
admin.site.register(Car, DraggableMPTTAdmin)

# Register your models here.
