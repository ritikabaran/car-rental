from django.contrib import admin
from booking.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(from_to)
admin.site.register(bookHistory)
admin.site.register(carPrice)