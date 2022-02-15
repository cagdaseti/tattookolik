from django.urls import path
from .views import (
    carousel_list,
    carousel_create,
    carousel_update,
    )


urlpatterns = [
    path('carousel_list/', carousel_list, name='carousel_list'), 
    path('carousel_create/', carousel_create, name='carousel_create'), 
    path('carousel_update/', carousel_update, name='carousel_update'), 
] 