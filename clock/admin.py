from django.contrib import admin

# Register your models here.
from .models import Data, MultipleImageUpload

admin.site.register(Data)
admin.site.register(MultipleImageUpload)