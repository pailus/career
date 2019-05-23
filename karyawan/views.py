from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Karyawan
from .forms import KaryawanForm

def DaftarKaryawan(request):
    # data = list(Karyawan.objects.all().values('id', 'nama','jabatan__nama','pendidikan__nama'))
    # return JsonResponse(data, safe=False)
    form = KaryawanForm()
    karyawan = Karyawan.objects.all()
    print(form)
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'daftar_karyawan.html',{'karyawan':karyawan, 'form':form})
# Create your views here.
