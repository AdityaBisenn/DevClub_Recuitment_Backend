from django.contrib import admin
from .models import Member, Staff, Sport, Court, Slot

# Register your models here.
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Sport)
admin.site.register(Court)
admin.site.register(Slot)
