from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(SocialMedia)
admin.site.register(MetaTag)