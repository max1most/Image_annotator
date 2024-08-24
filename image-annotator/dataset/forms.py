from django import forms
from .models import DatasetcreatorProfilDataset , DatasetcreatorKonfigurasi

TYPEDATA = (
    ('', 'Choose...'),
    ('Image', 'Image'),
    ('Video', 'Video'),
)

CONFIGURATION = (
    ('', 'Choose...'),
    ('1', 'Configuration 1'),
    ('2', 'Configuration 2'),
    ('3', 'Add Configuration'),
)

class DatasetcreatorProfileDatasetForm(forms.ModelForm):
    id_profil_dataset = forms.CharField(required=False)
    nama_dataset = forms.CharField(required=False)
    deskripsi = forms.CharField(required=False, widget=forms.Textarea)
    tanggal_buat = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    type_data = forms.ChoiceField(choices=TYPEDATA, required=False)
    configuration = forms.ModelChoiceField(queryset= DatasetcreatorKonfigurasi.objects.all())
    
    class Meta:
        model = DatasetcreatorProfilDataset
        fields = ['id_profil_dataset', 'nama_dataset', 'deskripsi', 'tanggal_buat', 'type_data', 'configuration']


# class DatasetcreatorProfileDatasetForm(forms.ModelForm):
#     class Meta:
#         model = DatasetcreatorProfilDataset
#         fields ='__all__'
        


