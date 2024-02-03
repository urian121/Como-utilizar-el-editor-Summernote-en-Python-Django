
from django.urls import path

from . views import inicio

urlpatterns = [
    path('admin/', inicio, name='inicio'),
]
