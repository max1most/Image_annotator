from django.db import models
from django.urls import include, path

# class Pengguna(models.Model):
#     id_pengguna =  models.BigIntegerField( primary_key=True)
#     nama_pengguna = models.CharField(max_length=50)
#     nama_lengkap = models.CharField(max_length=50)
#     email = models.EmailField((""), max_length=50)
#     password = models.CharField(max_length=15)
#     is_active = models.CharField(max_length=1)


# class Profil_dataset(models.Model):
#     id_profil_dataset = models.BigIntegerField( primary_key=True)
#     id_pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
#     nama_dataset = models.CharField(max_length=50)
#     deskripsi = models.CharField(max_length=225, null=True)
#     id_pembuat = models.IntegerField()
#     tanggal_buat = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['nama_dataset','-tanggal_buat']


 
# class Konfigurasi(models.Model):
#     id_konfigurasi = models.BigIntegerField( primary_key=True)
#     id_profil_dataset = models.ForeignKey(Profil_dataset, max_length=19, on_delete=models.CASCADE)
#     metode_stratifikasi = models.CharField(max_length=10)
#     path_file_konfigurasi = models.CharField(max_length=50)
#     id_pembuat = models.ForeignKey(Pengguna, max_length=11, on_delete=models.CASCADE)
#     tanggal_buat = models.DateTimeField(auto_now=True)
#     tanggal_modifikasi = models.DateTimeField(auto_now=True)
#     nama_split = models.CharField(max_length=20)
#     is_balance = models.CharField(max_length=1)
#     k_fold = models.IntegerField()
     

# class Konfigurasi_split(models.Model): 
#     id_konfigurasi_split = models.BigIntegerField( primary_key=True)
#     id_konfigurasi = models.ForeignKey(Konfigurasi, max_length=19, on_delete=models.CASCADE)
#     split_type = models.CharField(max_length=1)
#     persen_split = models.DecimalField(max_digits=5, decimal_places=2)
    

#     # class Meta:
#     #     ordering = ['nama_konfigurasi','tanggal_buat']

#     def is_balance_status(self):
#         if self.is_balance == 1:
#             return "balance"
#         else:
#             return "imbalance"

# class Kategori_kelas(models.Model):
#     id_kategori_kelas = models.IntegerField(primary_key=True)
#     nama_ketegori = models.CharField(max_length=50)
#     jenis_kontributor = models.CharField(max_length=1)

# class Sub_kategori_kelas(models.Model):
#     id_sub_kategori_kelas = models.IntegerField(primary_key=True)
#     id_kategori_kelas = models.ForeignKey(Kategori_kelas, max_length=19, on_delete=models.CASCADE) 
#     nama_sub_kategori = models.CharField(max_length=100)
#     jenis_kontributor = models.CharField(max_length=1)       

# class Kelas(models.Model):
#     id_kelas = models.BigIntegerField(primary_key=True)
#     id_sub_kategori_kelas = models.ForeignKey(Sub_kategori_kelas, on_delete=models.CASCADE) 
 

    


#     class Meta:
#         managed = False
#         db_table = 'Sub_kategori_kelas' 
    
# class Konfigurasi_kelas(models.Model):
#     id_konfigurasi_kelas = models.IntegerField(primary_key=True)
#     id_kelas = models.ForeignKey(Kelas, max_length=19, on_delete=models.CASCADE)  
#     porsi = models.DecimalField(max_digits=5, decimal_places=2)

# class Job_item(models.Model):
#     id_job_item = models.BigIntegerField(primary_key=True)
#     id_profile_job = models.IntegerField()  
#     id_gambar = models.ForeignKey(Kelas, max_length=19, on_delete=models.CASCADE)  
#     id_job_assigment_annotator = models.IntegerField()
#     id_job_reviewer = models.IntegerField()
#     status_pekerjaan = models.CharField(max_length=1)
    
    
# class Hasil_dataset(models.Model):
#     id_hasil_dataset = models.BigIntegerField( primary_key=True)
#     id_profil_dataset = models.ForeignKey(Profil_dataset, max_length=19, on_delete=models.CASCADE)
#     id_job_item = models.ForeignKey(Job_item, max_length=19, on_delete=models.CASCADE)
#     id_konfigurasi_split = models.ForeignKey(Konfigurasi_split, max_length=11, on_delete=models.CASCADE)
#     tipe_hasil_dataset = models.IntegerField()
#     id_pembuat = models.IntegerField()
#     tanggal_buat = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-tanggal_buat']


# class Histori_penggunaan(models.Model):
#     id_histori_penggunaan = models.BigIntegerField( primary_key=True)
#     id_hasil_dataset = models.ForeignKey(Hasil_dataset, max_length=19, on_delete=models.CASCADE)
#     id_pengguna = models.IntegerField()
#     remark = models.CharField(max_length=500)


# class User_chat(models.Model):
#     id_user_chat =  models.BigIntegerField( primary_key=True)
#     id_hasil_dataset = models.ForeignKey(Hasil_dataset, max_length=19, on_delete=models.CASCADE)
#     id_parent_user_chat = models.IntegerField() 
#     pesan =  models.CharField(max_length=200)
#     tanggal_buat = models.DateTimeField(auto_now=True)
    


# class Sumber_data(models.Model):
#     id_sumber_data =  models.BigIntegerField( primary_key=True)
#     id_konfigurasi = models.ForeignKey(Konfigurasi, max_length=19, on_delete=models.CASCADE)
#     id_job_item = models.ForeignKey(Job_item, max_length=19, on_delete=models.CASCADE) #########


# class Segmentasi_dataset(models.Model):
#     id_segmentasi_dataset = models.BigIntegerField( primary_key=True)
#     id_hasil_datset = models.ForeignKey(Hasil_dataset, max_length=19, on_delete=models.CASCADE)
#     id_tipe_segmentasi = models.IntegerField()
#     label_segmentasi = models.CharField(max_length=20)
#     warna_segmentasi = models.CharField(max_length=10)
#     koordinat = models.IntegerField()


# class Segmentasi_detail_dataset(models.Model):
#     id_segmentasi_detail_dataset = models.BigIntegerField( primary_key=True)
#     id_segmentasi_dataset = models.ForeignKey(Segmentasi_dataset, max_length=19, on_delete=models.CASCADE)
#     koordinat_x = models.IntegerField()
#     koordinat_y = models.IntegerField()


# class Anotasi_dataset(models.Model):
#     id_anootasi_dataset = models.BigIntegerField( primary_key=True)
#     id_segmentasi_dataset = models.ForeignKey(Segmentasi_dataset, max_length=19, on_delete=models.CASCADE)
#     koordinat_x = models.IntegerField()
#     koordinat_y = models.IntegerField()
#     lebar = models.IntegerField()
#     tinggi = models.IntegerField()


# class Polygon_dataset(models.Model):
#     id_polygon_tool = models.BigIntegerField( primary_key=True)
#     id_anotasi_dataset = models.ForeignKey(Anotasi_dataset, max_length=19, on_delete=models.CASCADE)
#     id_anotasi = models.IntegerField()
#     koordinat_xn = models.IntegerField()
#     koordinat_yn = models.IntegerField()


class DatasetcreatorAnotasiDataset(models.Model):
    id_anootasi_dataset = models.BigIntegerField(primary_key=True)
    koordinat_x = models.IntegerField()
    koordinat_y = models.IntegerField()
    lebar = models.IntegerField()
    tinngi = models.IntegerField()
    id_segmentasi_dataset = models.ForeignKey('DatasetcreatorSegmentasiDataset', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'datasetcreator_anotasi_dataset'


class DatasetcreatorHasilDataset(models.Model):
    id_hasil_dataset = models.BigIntegerField(primary_key=True)
    tipe_hasil_dataset = models.IntegerField()
    tanggal_buat = models.DateTimeField()
    id_job_item = models.ForeignKey('DatasetcreatorJobItem', models.DO_NOTHING)
    id_konfigurasi_split = models.ForeignKey('DatasetcreatorKonfigurasiSplit', models.DO_NOTHING)
    id_profil_dataset = models.ForeignKey('DatasetcreatorProfilDataset', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'datasetcreator_hasil_dataset'


class DatasetcreatorHistoriPenggunaan(models.Model):
    id_histori_penggunaan = models.BigIntegerField(primary_key=True)
    id_pengguna = models.IntegerField()
    remark = models.CharField(max_length=500)
    id_hasil_dataset = models.ForeignKey(DatasetcreatorHasilDataset, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'datasetcreator_histori_penggunaan'


class DatasetcreatorJobItem(models.Model):
    id_job_item = models.BigIntegerField(primary_key=True)
    id_profile_job = models.IntegerField()
    id_job_assigment_annotator = models.IntegerField()
    id_job_reviewer = models.IntegerField()
    status_pekerjaan = models.CharField(max_length=1)
    id_gambar_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_job_item'


class DatasetcreatorKategoriKelas(models.Model):
    id_kategori_kelas = models.IntegerField(primary_key=True)
    nama_ketegori = models.CharField(max_length=50)
    jenis_kontributor = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'datasetcreator_kategori_kelas'


class DatasetcreatorKonfigurasi(models.Model):
    id_konfigurasi = models.BigIntegerField(primary_key=True)
    metode_stratifikasi = models.CharField(max_length=10)
    image_origin = models.CharField(max_length=50)
    tanggal_buat = models.DateTimeField()
    tanggal_modifikasi = models.DateTimeField()
    nama_split = models.CharField(max_length=20)
    is_balance = models.CharField(max_length=1)
    k_fold = models.IntegerField()
    # id_profil_dataset = models.models.CharField(max_length=50, null=True)

    class Meta:
        managed = False
        db_table = 'datasetcreator_konfigurasi'


class DatasetcreatorKonfigurasiKelas(models.Model):
    id_konfigurasi_kelas = models.IntegerField(primary_key=True)
    porsi = models.DecimalField(max_digits=5, decimal_places=2)
    id_kelas_id = models.BigIntegerField()
    id_konfigurasi = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_konfigurasi_kelas'


class DatasetcreatorKonfigurasiSplit(models.Model):
    id_konfigurasi_split = models.BigIntegerField(primary_key=True)
    split_type = models.CharField(max_length=1)
    persen_split = models.DecimalField(max_digits=5, decimal_places=2)
    id_konfigurasi_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_konfigurasi_split'


class DatasetcreatorPengguna(models.Model):
    id_pengguna = models.BigIntegerField(primary_key=True)
    nama_pengguna = models.CharField(max_length=50)
    nama_lengkap = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    is_active = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'datasetcreator_pengguna'


class DatasetcreatorPolygonDataset(models.Model):
    id_polygon_tool = models.BigIntegerField(primary_key=True)
    id_anotasi = models.IntegerField()
    koordinat_xn = models.IntegerField()
    koordinat_yn = models.IntegerField()
    id_anotasi_dataset_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_polygon_dataset'


class DatasetcreatorProfilDataset(models.Model):
    id_profil_dataset = models.BigIntegerField(primary_key=True)
    nama_dataset = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=225, blank=True, null=True)
    id_pembuat = models.IntegerField()
    tanggal_buat = models.DateTimeField()
    id_pengguna_id = models.BigIntegerField()
    type_data = models.CharField(max_length=15)
    configuration = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nama_dataset

    class Meta:
        managed = False
        db_table = 'datasetcreator_profil_dataset'


class DatasetcreatorSegmentasiDataset(models.Model):
    id_segmentasi_dataset = models.BigIntegerField(primary_key=True)
    id_tipe_segmentasi = models.IntegerField()
    label_segmentasi = models.CharField(max_length=20)
    warna_segmentasi = models.CharField(max_length=10)
    koordinat = models.IntegerField()
    id_hasil_datset_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_segmentasi_dataset'


class DatasetcreatorSegmentasiDetailDataset(models.Model):
    id_segmentasi_detail_dataset = models.BigIntegerField(primary_key=True)
    koordinat_x = models.IntegerField()
    koordinat_y = models.IntegerField()
    id_segmentasi_dataset_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_segmentasi_detail_dataset'


class DatasetcreatorSubKategoriKelas(models.Model):
    id_sub_kategori_kelas = models.IntegerField(primary_key=True)
    nama_sub_kategori = models.CharField(max_length=100)
    jenis_kontributor = models.CharField(max_length=1)
    id_kategori_kelas_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_sub_kategori_kelas'


class DatasetcreatorSumberData(models.Model):
    id_sumber_data = models.BigIntegerField(primary_key=True)
    id_job_item_id = models.BigIntegerField()
    id_konfigurasi_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_sumber_data'


class DatasetcreatorUserChat(models.Model):
    id_user_chat = models.BigIntegerField(primary_key=True)
    id_parent_user_chat = models.IntegerField()
    pesan = models.CharField(max_length=200)
    tanggal_pesan = models.DateTimeField()
    id_hasil_dataset_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetcreator_user_chat'