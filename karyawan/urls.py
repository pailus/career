from django.conf.urls import url, include # untuk import urls dan include
from karyawan import views # menngambil semua function yang ada di app karyawan views.py 

urlpatterns = [
    url(r'daftar/', views.DaftarKaryawan, name='daftarKaryawan'),
]
