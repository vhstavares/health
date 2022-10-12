from django.urls import path

from . import views

urlpatterns = [
    path('', views.person, name='person'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('create_person/', views.create_person, name='create_person'),
    path('update_person/<id>', views.update_person, name='update_person'),
    path('delete_person/<id>', views.delete_person, name='delete_person'),
    path('create_vehicle/', views.create_vehicle, name='create_vehicle'),
    path('update_vehicle/<id>', views.update_vehicle, name='update_vehicle'),
    path('delete_vehicle/<id>', views.delete_vehicle, name='delete_vehicle'),
]