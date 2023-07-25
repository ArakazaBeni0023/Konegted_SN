from django.contrib import admin
from .models import *

@admin.register(Konegted_SN)
class Konegted_SNAdmin(admin.ModelAdmin):
    list_display = "nom", "prenom"

admin.site.register(Parent)
admin.site.register(Formateur)

