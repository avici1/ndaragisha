from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LostItems)
admin.site.register(FoundItems)
admin.site.register(IncomingMessage)