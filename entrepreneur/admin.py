from django.contrib import admin
from .models import entrepreneur
# Register your models here.

@admin.register(entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
  list_display= ["id","name","email"]
