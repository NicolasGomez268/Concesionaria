from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'marca', 'modelo', 'año', 'precio', 'estado', 'kilometraje', 
            'combustible', 'color', 'descripcion', 
            'imagen_destacada', 'activo'
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'combustible': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'imagen_destacada': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_imagenes(self):
        imagenes = self.files.getlist('imagenes')
        if len(imagenes) > 7:
            raise forms.ValidationError('Solo se permiten hasta 7 imágenes adicionales.')
        return imagenes 