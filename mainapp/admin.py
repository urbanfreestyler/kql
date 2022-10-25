from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(MetaTag)
admin.site.register(Application)