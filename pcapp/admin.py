from django.contrib import admin
from .models import Datas
from .models import Appointment


# Register your Datas
admin.site.register(Datas)

# Register your appointment
admin.site.register(Appointment)
