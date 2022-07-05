from django.urls import path
from .views import *

urlpatterns = [
    path('',t_principal),
    path('Sofia/',t_sofia),
    path('Ernesto/',t_ernesto),
    path('Marisa/',t_marisa),
    path('Alejo/',t_alejo),
    path('Tadeo/',t_tadeo)
]