from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list, name='note_list')
]
