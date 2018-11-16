from django import forms
"""
class AgregarMascotas(forms.Form):
    fotoMascota=forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre Mascota")
    raza=forms.CharField(widget=forms.TextInput(),label="Raza Mascota")
    descripcion=forms.CharField(widget = forms.Textarea(attrs = { "placeholder": "Ingrese descripción" }), label = "Descripción")
    estado=forms.ChoiceField(choices=ESTADO, initial='Rescatado')
    """