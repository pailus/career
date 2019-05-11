from django.db import models

# Create your models here.
class Pendidikan(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    def __str__(self):
        return self.nama


class Jabatan(models.Model):
    nama = models.CharField( max_length=50)
    keterangan = models.CharField(max_length=50)
    def __str__(self):
        return self.nama

class Karyawan(models.Model):
    nama = models.CharField(max_length=50)
    pendidikan = models.ForeignKey(Pendidikan, on_delete=models.CASCADE)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    telpon = models.CharField(max_length=13)
    def __str__(self):
        return self.nama
