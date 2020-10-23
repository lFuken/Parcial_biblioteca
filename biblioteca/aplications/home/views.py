from django.shortcuts import render
from django.urls import reverse_lazy
from aplications.usuario.models import Usuario
from aplications.libro.models import Libro
from aplications.autor.models import autor
from aplications.prestamos.models import prestamo
# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView

class HomeView(TemplateView):
    template_name = "home/home.html"

#---------------------------- CREATE VIEW-----------------------#
class UsuarioCreateView(CreateView):
    template_name = "home/usuario.html"
    model = Usuario
    fields = ('__all__')
    success_url='.'

class LibroCreateView(CreateView):
    template_name = "home/libro.html"
    model = Libro
    fields = ('__all__')
    success_url='.'

class AutorCreateView(CreateView):
    template_name = "home/autor.html"
    model = autor
    fields = ('__all__')
    success_url='.'

class PrestamoCreateView(CreateView):
    template_name = "home/prestamo.html"
    model = prestamo
    fields = ('__all__')
    success_url='.'

#------------------------------LIST VIEW-----------------------------#
class ListarUsuarioListView(ListView):
    cl= Usuario.objects.prefetch_related()
    queryset=cl
    fields=('__all__')
    template_name = "home/listar_usuario.html"
    context_object_name = 'usuario'    

class ListarLibroListView(ListView):
    cl= Libro.objects.prefetch_related()
    queryset=cl
    fields=('__all__')
    template_name = "home/listar_libro.html"
    context_object_name = 'libro'

class ListarAutorListView(ListView):
    Rv= autor.objects.prefetch_related()
    queryset=Rv
    fields=('__all__')
    template_name = "home/listar_autor.html"
    context_object_name = 'autor'  

class ListarPrestamoListView(ListView):
    Rv= prestamo.objects.prefetch_related()
    queryset=Rv
    fields=('__all__')
    template_name = "home/listar_prestamo.html"
    context_object_name = 'prestamo' 

#---------------------------------UPDATE VIEW-------------------------#

class successView(TemplateView):
    template_name = "home/success.html"

class UsuarioUpdateView(UpdateView):
    template_name = "home/actualizar_usuario.html"
    model = Usuario
    fields = ('__all__')
    success_url = '.'

class LibroUpdateView(UpdateView):
    template_name = "home/actualizar_libro.html"
    model = Libro
    fields = ('__all__')
    success_url = '.'

class AutorUpdateView(UpdateView):
    template_name = "home/actualizar_autor.html"
    model = autor
    fields = ('__all__')
    success_url = '.'

class PrestamoUpdateView(UpdateView):
    template_name = "home/actualizar_Prestamo.html"
    model = prestamo
    fields = ('__all__')
    success_url = '.'

#---------------------------------DELETE VIEW-------------------------#

class UsuarioDeleteView(DeleteView):
    template_name = "home/eliminar_usuario.html"
    model = Usuario
    fields = ('__all__')
    success_url = reverse_lazy('home_app:elim')

class LibroDeleteView(DeleteView):
    template_name = "home/eliminar_libro.html"
    model = Libro
    fields = ('__all__')
    success_url = reverse_lazy('home_app:elim')

class AutorDeleteView(DeleteView):
    template_name = "home/eliminar_autor.html"
    model = autor
    fields = ('__all__')
    success_url = reverse_lazy('home_app:elim')

class PrestamoDeleteView(DeleteView):
    template_name = "home/eliminar_prestamo.html"
    model = prestamo
    fields = ('__all__')
    success_url = reverse_lazy('home_app:elim')
