from django.urls import path
from core.views import doctor_create, doctor_delete, doctor_list, doctor_update
from core import views

app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    

    path('cargo_list/', views.cargo_list, name='cargo_list'),
    path('cargo_update/<int:id>/', views.cargo_update, name='cargo_update'),
    path('cargo_crear/', views.crear_cargo, name='cargo_crear'),
    path('cargo_eliminar/<int:id>/', views.borrar_cargo, name='cargo_eliminar'),
    
    path('empleados/', views.Empleado_list, name='empleados'),
    path('empleados_create/', views.crear_empleado, name='empleados_create'),
    path('empleados_delete/<int:id>/', views.borrar_empleado, name='empleados_delete'),
    path('empleados_update/<int:id>/', views.Empleado_update, name='empleados_update'),

    path('departamento_list/',views.departamento_list, name='departamento_list'),
    path('departamento_crear/',views.crear_departamento, name='departamento_crear'),
    path('departamento_eliminar/<int:id>/', views.borrar_departamento,name='departamento_eliminar'),
    path('departamento_update/<int:id>/', views.departamento_update,name='departamento_update'),

    path('rol_list/',views.Rol_list, name='rol_list'),
    path('rol_crear/',views.crear_Rol, name='rol_crear'),
    path('rol_eliminar/<int:id>/', views.borrar_Rol,name='rol_eliminar'),
    path('rol_update/<int:id>/', views.Rol_update,name='rol_update'),

    path('Contrato_list',views.contrato_list, name='Contrato_list'),
    path('Contrato_crear',views.crear_contrato, name='Contrato_crear'),
    path('Contrato_update/<int:id>/', views.contrato_update,name='Contrato_update'),
    path('Contrato_eliminar/<int:id>/', views.borrar_contrato,name='Contrato_eliminar'),


    path('prestamo_list/', views.prestamo_list, name='prestamo_list'),
    path('crear_prestamo/', views.crear_prestamo, name='crear_prestamo'), 
    path('prestamo_list/', views.prestamo_list, name='prestamo_list'), 
    path('prestamo_list/', views.prestamo_list, name='prestamo_list'), 

    path('doctor_list/',doctor_list, name='doctor_list'),  # URL para la vista home
    path('doctor_create/',doctor_create, name='doctor_create'),  # URL para la vista home
    path('doctor_update/<int:id>/', doctor_update,name='doctor_update'),
    path('doctor_delete/<int:id>/', doctor_delete,name='doctor_delete'),
]
