from django import forms
from .models import Karyawan

class KaryawanForm(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = '__all__'