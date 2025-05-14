from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select
from django import forms
from .models import Doctor
from .models import Empleado,Cargo,TipoContrato,Rol,Departamento, Prestamo
class DoctorForm(ModelForm):
    # Definir las opciones para el combobox de especialidades
    SPECIALTY_CHOICES = [
        ('', 'Seleccione una especialidad'),
        ('Medicina General', 'Medicina General'),
        ('Cardiología', 'Cardiología'),
        ('Dermatología', 'Dermatología'),
        ('Neurología', 'Neurología'),
        ('Pediatría', 'Pediatría'),
        ('Ginecología', 'Ginecología'),
        ('Oftalmología', 'Oftalmología'),
        ('Traumatología', 'Traumatología'),
        ('Psiquiatría', 'Psiquiatría'),
        ('Odontología', 'Odontología'),
    ]
    
    # Sobreescribir el campo specialty para convertirlo en un select
    # Esto reemplaza el campo CharField del modelo con un campo de selección en el formulario
    specialty = forms.ChoiceField(
        choices=SPECIALTY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Doctor
        # fields = ['name',' email','phone','specialty']
        #cada campo lo convierte a un control html <input type="text" name="name" id="name" class="form-control" placeholder="Nombre del doctor" required>
        fields = '__all__'
        # exclude = ['phone']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'honorarios': NumberInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            # No incluimos specialty aquí porque ya lo definimos arriba
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'sexo': forms.Select(choices=Empleado.SEXO_CHOICES, attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sueldo': forms.NumberInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-select'}),
            'departamento': forms.Select(attrs={'class': 'form-select'}),
            'tipo_contrato': forms.Select(attrs={'class': 'form-select'}),
        }

class CargoForm(forms.ModelForm):

    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContratoForm(forms.ModelForm):

    class Meta:
        model = TipoContrato
        fields = '__all__'
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = ['empleado', 'aniomes', 'horas_extra', 'bono', 'iess', 'tot_ing', 'tot_des', 'neto']
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'aniomes': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horas_extra': forms.NumberInput(attrs={'class': 'form-control'}),
            'bono': forms.NumberInput(attrs={'class': 'form-control'}),
            'iess': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tot_ing': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'tot_des': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'neto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }


class PrestamoForm(forms.ModelForm):

    class Meta:
        model=Prestamo
        fields= ['empleado', 'tipo_prestamo', 'fecha_prestamo', 'monto', 'interes', 'monto_pagar', 'numero_cuotas', 'cuota_mensual', 'saldo']
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'tipo_prestamo': forms.Select(attrs={'class': 'form-select'}) ,
            'fecha_prestamo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'interes': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto_pagar': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_cuotas': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuota_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control'})
        }
