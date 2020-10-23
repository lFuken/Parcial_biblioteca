from django.contrib import admin
from django.urls import path

from.import views

app_name = "home_app"

urlpatterns = [
    path('success/', views.successView.as_view(), name = 'elim'),

    path('usuario/', views.UsuarioCreateView.as_view()),
    path('libro/', views.LibroCreateView.as_view()),
    path('autor/', views.AutorCreateView.as_view()),
    path('prestamo/', views.PrestamoCreateView.as_view()),

    path('listar_usuario/', views.ListarUsuarioListView.as_view()),
    path('listar_libro/', views.ListarLibroListView.as_view()),
    path('listar_autor/', views.ListarAutorListView.as_view()),
    path('listar_prestamo/', views.ListarPrestamoListView.as_view()),

    path('actualizar_usuario/<pk>/', views.UsuarioUpdateView.as_view()),
    path('actualizar_libro/<pk>/', views.LibroUpdateView.as_view()),
    path('actualizar_autor/<pk>/', views.AutorUpdateView.as_view()),
    path('actualizar_prestamo/<pk>/', views.PrestamoUpdateView.as_view()),


    path('eliminar_usuario/<pk>/', views.UsuarioDeleteView.as_view()),
    path('eliminar_libro/<pk>/', views.LibroDeleteView.as_view()),
    path('eliminar_autor/<pk>/', views.AutorDeleteView.as_view()),
    path('eliminar_prestamo/<pk>/', views.PrestamoDeleteView.as_view()),
]