from django.contrib import admin
from .models import RawTransaction, RealTransaction, TagLookup

# Register your models here.

admin.site.register(RawTransaction)
admin.site.register(RealTransaction)
admin.site.register(TagLookup)
