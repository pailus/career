from django.contrib import admin

# Register your models here.
from .models import * 

class KaryawanAdmin(admin.ModelAdmin):
    list_display = ('nama','jabatan','pendidikan')
admin.site.register(Jabatan)
admin.site.register(Pendidikan)
admin.site.register(Karyawan, KaryawanAdmin)