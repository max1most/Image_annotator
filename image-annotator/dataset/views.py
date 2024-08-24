from django.shortcuts import render, get_object_or_404
from .forms import DatasetcreatorProfileDatasetForm
from .models import DatasetcreatorKonfigurasi
from .models import DatasetcreatorHasilDataset
from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect


def datasetcreator(request):
    form = DatasetcreatorProfileDatasetForm()
    context = None
    if request.method == 'POST':
        if 'submit' in request.POST:  
            if form.is_valid():
                id_profil_dataset = form.id_profil_dataset['id_profile_dataset']
                nama_dataset = form.nama_dataset['nama_dataset']
                deskripsi = form.deskripsi['deskripsi']
                tanggal_buat = form.tanggal_buat ['tanggal_buat']
                type_data = form.type_data['type_data']
                configuration = form.configuration['configuration']
                konfigurasi_items =DatasetcreatorKonfigurasi.objects.filter(id_konfigurasi = configuration_id)
                new_config = DatasetcreatorKonfigurasi.objects.create(metode_stratifikasi =konfigurasi_items.metode_stratifikasi, image_origin=konfigurasi_items.image_origin, tanggal_buat=konfigurasi_items.tanggal_buat, 
                                                                      tanggal_modifikasi=konfigurasi_items.tanggal_modifikasi, nama_split=konfigurasi_items.nama_split, is_balance=konfigurasi_items.is_balance, 
                                                                      k_fold=konfigurasi_items.k_fold,)
             
                DatasetcreatorProfile = ProfileDataset.object.create(id_profile_dataset=id_profile_dataset, nama_dataset=nama_dataset, deskripsi=deskripsi, 
                                                                        tanggal_buat=tanggal_buat , type_data=type_data, configuration=new_config)
                 
                
                form.save()  # This saves the form data into the database
                return render('hasilcomfig.html')
            
        if 'viewconfig' in request.POST:
            configuration_id = request.POST.get('configuration')  # Correct spelling and use `get`
            print(configuration_id)
            konfigurasi_items =DatasetcreatorKonfigurasi.objects.filter(id_konfigurasi = configuration_id)
            return render(request, 'viewconfig.html', {'konfigurasi_items': konfigurasi_items})
    
    else: 
        context = {
            'form': form , 
        }
    
    # Render the initial form if not a POST request or if the 'viewconfig' key is not in the POST data
        return render(request, 'index.html', context)

def DatasetcreatorProfil(request):
    if request.method == 'POST':
        form = DatasetcreatorProfileDatasetForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data into the database
            return redirect('success_page')  # Redirect after successful submission
    else:
        form = DatasetcreatorProfileDatasetForm()
        
    return render(request, 'index.html', {'form': form})

def viewconfig(request):
    konfigurasi_items = DatasetcreatorKonfigurasi.objects.all()  # atau filter sesuai kebutuhan
    return render(request, 'viewconfig.html', {'konfigurasi_items': konfigurasi_items})

def halamanconfig(request, id):
    konfigurasi_items = get_object_or_404(DatasetcreatorKonfigurasi, id_konfigurasi=id)
    print(konfigurasi_items)
    return render(request, 'halamanconfig.html', {'konfigurasi_items': konfigurasi_items})

def metodeconfig(request):
    konfigurasi_items = DatasetcreatorKonfigurasi.objects.all()
    return render(request, 'metodeconfig.html', {'konfigurasi_items': konfigurasi_items})

def hasilconfig(request):
    konfigurasi_items = DatasetcreatorHasilDataset.objects.all()
    return render(request, 'hasilconfig.html', {'konfigurasi_items': konfigurasi_items})

def viewhasil(request):
    konfigurasi_items = DatasetcreatorHasilDataset.objects.all()
    return render(request, 'viewhasil.html', {'konfigurasi_items': konfigurasi_items})