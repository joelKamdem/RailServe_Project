from django.contrib import admin

from Railserve_tracking.models import Device
from Railserve_tracking.models import Position
# Register your models here.

admin.site.register(Device)
admin.site.register(Position)


