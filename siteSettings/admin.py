from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Favicon)
admin.site.register(TagForHead)

admin.site.register(FirstBlock)
admin.site.register(SecondBlock)
admin.site.register(ThirdBlock)