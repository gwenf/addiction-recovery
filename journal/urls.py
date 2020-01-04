from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='journal'),
    path('<int:entry_id', views.entry, name='journal_entry'),
    path('create', views.create, name='journal_create')
]
