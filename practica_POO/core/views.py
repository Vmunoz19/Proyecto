from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from core.models import Doctor
from core.forms import DoctorForm,EmpleadoForm, CargoForm, DepartamentoForm,RolForm, ContratoForm, PrestamoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from core.models import Empleado,Rol,Cargo,Departamento, TipoContrato, Prestamo, TipoPrestamo
from django.db.models import Q


def home(request):
    data = {
        'title': 'Nomina Pro',
        'description': 'Gesion de nominas',
        'author': 'Grupo Laspi y Daniel Vera',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    #return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    #return JsonResponse(data)  
    return render(request, 'home.html', data)


def doctor_list(request):
    doctors = Doctor.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: doctors = Doctor.objects.filter(name__icontains=query)
    else: doctors = Doctor.objects.all()
    context = {'doctors': doctors, 'title': 'Listado de doctores'} 
    return render(request, 'doctor/list.html', context)


# vista:
def doctor_create(request):
    context={'title':'Ingresar Doctor'}
    print("metodo: ",request.method)
    if request.method == "GET":
        # print("entro por get")
        
        form = DoctorForm()# instancia el formulario con los campos vacios
        context['form'] = form
        return render(request, 'doctor/create.html', context)
    else:
        #  print("entro por post")
        form = DoctorForm(request.POST) # instancia el formulario con los datos del post
        if form.is_valid():
            form.save()
            # doctor = form.save(commit=False)# lo tiene en memoria
            # doctor.user = request.user
            # doctor.save() # lo guarda en la BD
            return redirect('core:doctor_list')
        else:
            context['form'] = form
            return render(request, 'doctor/create.html',context) 
        #return JsonResponse({"message": "voy a crear un doctor"})


def doctor_update(request,id):
   context={'title':'Actualizar Doctor'}
   doctor = Doctor.objects.get(pk=id)
   if request.method == "GET":
      form = DoctorForm(instance=doctor)# instancia el formulario con los datos del doctor
      context['form'] = form
      return render(request, 'doctor/create.html', context)
   else:
      form = DoctorForm(request.POST,instance=doctor)
      if form.is_valid():
          form.save()
          return redirect('core:doctor_list')
      else:
          context['form'] = form
          return render(request, 'doctor/create.html',context)

def doctor_delete(request,id):
    doctor=None
    try:
        doctor = Doctor.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Doctor a Eliminar','doctor':doctor,'error':''}
            return render(request, 'doctor/delete.html',context)  
        else: 
            doctor.delete()
            return redirect('core:doctor_list')
    except:
        context = {'title':'Datos del Doctor','doctor':doctor,'error':'Error al eliminar al doctor'}
        return render(request, 'doctor/delete.html',context)
    

# LOGIN

def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'login/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('core:empleados')
    
#Empleados
#@login_required
def Empleado_list(request):
    Empleados = Empleado.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: Empleados = Empleado.objects.filter(nombre__icontains=query)
    else: Empleados = Empleado.objects.all()
    context = {'Empleados': Empleados, 'title': 'Listado de doctores'} 
    return render(request, 'empleados/list.html', context)

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/create.html', {'form': form})

def borrar_empleado(request,id):
    empleado=None
    try:
        empleado = Empleado.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Doctor a Eliminar','doctor':empleado,'error':''}
            return render(request, 'empleados/delete.html',context)  
        else: 
            empleado.delete()
            return redirect('core:empleados')
    except:
        context = {'title':'Datos del Doctor','doctor':empleado,'error':'Error al eliminar al doctor'}
        return render(request, 'empleados/delete.html',context)

def Empleado_update(request,id):
   context={'title':'Actualizar Empleado'}
   empleado = Empleado.objects.get(pk=id)
   if request.method == "GET":
      form = EmpleadoForm(instance=empleado)# instancia el formulario con los datos del doctor
      context['form'] = form
      return render(request, 'empleados/create.html', context)
   else:
      form = EmpleadoForm(request.POST,instance=empleado)
      if form.is_valid():
          form.save()
          return redirect('core:empleados')
      else:
          context['form'] = form
          return render(request, 'empleados/create.html',context)


#Cargos
def crear_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:cargo_list')
    else:
        form = CargoForm()
    return render(request, 'cargo/create.html', {'form': form})

def cargo_list(request):
    Cargos = Cargo.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: Cargos = Cargo.objects.filter(descripcion__icontains=query)
    else: Cargos = Cargo.objects.all()
    context = {'cargo_list': Cargos, 'title': 'Listado de Cargos'} 
    return render(request, 'cargo/list.html', context)

def cargo_update(request,id):
   context={'title':'Actualizar Cargo'}
   cargos = Cargo.objects.get(pk=id)
   if request.method == "GET":
      form = CargoForm(instance=cargos)# instancia el formulario con los datos del doctor
      context['form'] = form
      return render(request, 'cargo/create.html', context)
   else:
      form = CargoForm(request.POST,instance=cargos)
      if form.is_valid():
          form.save()
          return redirect('core:cargo_list')
      else:
          context['form'] = form
          return render(request, 'cargo/create.html',context)

def borrar_cargo(request,id):
    cargo=None
    try:
        cargo = Cargo.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Cargo a Eliminar','doctor':cargo,'error':''}
            return render(request, 'cargo/delete.html',context)  
        else: 
            cargo.delete()
            return redirect('core:cargo_list')
    except:
        context = {'title':'Datos del Doctor','doctor':cargo,'error':'Error al eliminar al doctor'}
        return render(request, 'cargo/delete.html',context)

#Departamentos
def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:departamento_list')
    else:
        form = CargoForm()
    return render(request, 'departamento/create.html', {'form': form})

def departamento_list(request):
    Depart = Departamento.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: Depart = Departamento.objects.filter(descripcion__icontains=query)
    else: Depart = Departamento.objects.all()
    context = {'departamento_list': Depart, 'title': 'Listado de Departamentos'} 
    return render(request, 'departamento/list.html', context)

def departamento_update(request,id):
   context={'title':'Actualizar departamento'}
   depa = Departamento.objects.get(pk=id)
   if request.method == "GET":
      form = DepartamentoForm(instance=depa)# instancia el formulario con los datos del doctor
      context['form'] = form
      return render(request, 'departamento/create.html', context)
   else:
      form = DepartamentoForm(request.POST,instance=depa)
      if form.is_valid():
          form.save()
          return redirect('core:departamento_list')
      else:
          context['form'] = form
          return render(request, 'departamento/create.html',context)

def borrar_departamento(request,id):
    Depa=None
    try:
        Depa = Departamento.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Departamento a Eliminar','depa':Depa,'error':''}
            return render(request, 'departamento/delete.html',context)  
        else: 
            Depa.delete()
            return redirect('core:departamento_list')
    except:
        context = {'title':'Datos del Doctor','depa':Depa,'error':'Error al eliminar al doctor'}
        return render(request, 'departamento/delete.html',context)

#roles
def Rol_list(request):
    roles = Rol.objects.all().select_related('empleado')  # Optimización de consultas
    query = request.GET.get('q')
    
    if query:
        # Búsqueda segura por campos relacionados y normales
        roles = roles.filter(
            Q(empleado__nombre__icontains=query) |
            Q(empleado__cedula__icontains=query) |
            Q(aniomes__icontains=query)
        )
    
    context = {
        'Rol': roles,
        'title': 'Listado de roles',
        'query': query  # Para mantener el término de búsqueda en el template
    }
    return render(request, 'Rol/list.html', context)

def crear_Rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:rol_list')
    else:
        form = RolForm()
    empleados = Empleado.objects.all()
    return render(request, 'Rol/create.html', {'form': form, 'empleados': empleados})

def borrar_Rol(request,id):
    Roles=None
    try:
        Roles = Rol.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Rol a Eliminar','roles':Roles,'error':''}
            return render(request, 'Rol/delete.html',context)  
        else: 
            Roles.delete()
            return redirect('core:rol_list')
    except:
        context = {'title':'Datos del Rol','roles':Roles,'error':'Error al eliminar el Rol'}
        return render(request, 'Rol/delete.html',context)

def Rol_update(request, id):
    rol = get_object_or_404(Rol, pk=id)
    empleados = Empleado.objects.all()  
    if request.method == "POST":
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            return redirect('core:rol_list')
    else:
        form = RolForm(instance=rol)

    context = {
        'form': form,
        'empleados': empleados,
        'rol': rol,  
        'title': 'Actualizar Rol',
    }
    return render(request, 'Rol/create.html', context)

#tipo contrato

def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:Contrato_list')
    else:
        form = ContratoForm()
    return render(request, 'contrato/create.html', {'form': form})

def contrato_list(request):
    Contrato = TipoContrato.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: Contrato = TipoContrato.objects.filter(descripcion__icontains=query)
    else: Contrato = TipoContrato.objects.all()
    context = {'Contrato_list': Contrato, 'title': 'Listado de contratos'} 
    return render(request, 'contrato/list.html', context)

def contrato_update(request,id):
   context={'title':'Actualizar Contrato'}
   contrato = TipoContrato.objects.get(pk=id)
   if request.method == "GET":
      form = ContratoForm(instance=contrato)
      context['form'] = form
      return render(request, 'contrato/create.html', context)
   else:
      form = ContratoForm(request.POST,instance=contrato)
      if form.is_valid():
          form.save()
          return redirect('core:Contrato_list')
      else:
          context['form'] = form
          return render(request, 'contrato/create.html',context)

def borrar_contrato(request,id):
    contrato=None
    try:
        contrato = TipoContrato.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Contrato a Eliminar','empleado':contrato,'error':''}
            return render(request, 'contrato/delete.html',context)  
        else: 
            contrato.delete()
            return redirect('core:Contrato_list')
    except:
        context = {'title':'Datos del Doctor','doctor':contrato,'error':'Error al eliminar al doctor'}
        return render(request, 'contrato/delete.html',context)

#
def prestamo_list(request):
    prestamo = Prestamo.objects.all()
    print(request.method)
    print(request.GET)
    #return JsonResponse(list(doctors.values()), safe=False)
    query= request.GET.get('q',None)
    print(query)
    if query: prestamo = Prestamo.objects.filter(empleado__icontains=query)
    else: prestamo = Prestamo.objects.all()
    context = {'prestamo_list': prestamo, 'title': 'Listado de prestamos'} 
    return render(request, 'prestamo/list.html', context)

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:prestamo_list')
    else:
        form = PrestamoForm()
    return render(request, 'prestamo/create.html', {'form': form})

def borrar_prestamo(request,id):
    empleado=None
    try:
        empleado = Empleado.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Doctor a Eliminar','doctor':empleado,'error':''}
            return render(request, 'empleados/delete.html',context)  
        else: 
            empleado.delete()
            return redirect('core:empleados')
    except:
        context = {'title':'Datos del Doctor','doctor':empleado,'error':'Error al eliminar al doctor'}
        return render(request, 'empleados/delete.html',context)

def prestamo_update(request,id):
   context={'title':'Actualizar Empleado'}
   empleado = Empleado.objects.get(pk=id)
   if request.method == "GET":
      form = EmpleadoForm(instance=empleado)# instancia el formulario con los datos del doctor
      context['form'] = form
      return render(request, 'empleados/create.html', context)
   else:
      form = EmpleadoForm(request.POST,instance=empleado)
      if form.is_valid():
          form.save()
          return redirect('core:empleados')
      else:
          context['form'] = form
          return render(request, 'empleados/create.html',context)
