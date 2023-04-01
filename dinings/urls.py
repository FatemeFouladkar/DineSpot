from django.urls import path
from .views import MapView, CreateDining


app_name = 'dinings'

urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('add-dining', CreateDining.as_view(), name='add-dining')
]
