from django.contrib import admin
from core.models import Doctor
from .models import Cargo, Departamento, TipoContrato,Empleado, Rol, TipoPrestamo, Prestamo
# Register your models here.

admin.site.site_header = "App Medica"
admin.site.site_title = "Bienvenido a App Medica"
admin.site.register(Doctor)
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
admin.site.register(Empleado)
admin.site.register(TipoPrestamo)
admin.site.register(Prestamo)
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    readonly_fields = ('iess', 'tot_ing', 'tot_des', 'neto')
    list_display = ('empleado', 'aniomes', 'neto')