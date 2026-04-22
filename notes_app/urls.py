from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Notes CRUD
    path('notes/create/', views.create_note_view, name='create_note'),
    path('notes/<int:pk>/', views.detail_note_view, name='detail_note'),
    path('notes/<int:pk>/edit/', views.edit_note_view, name='edit_note'),
    path('notes/<int:pk>/delete/', views.delete_note_view, name='delete_note'),
    path('notes/<int:pk>/pin/', views.toggle_pin_view, name='toggle_pin'),
]
