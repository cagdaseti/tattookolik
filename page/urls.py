from django.urls import path
from .views import (
    # manage
    manage_list,

    # carousel
    carousel_list,
    carousel_create,
    carousel_update,

    # page
    page_list,
    page_create,
    page_update,
    page_delete,
    )


app_name = "page"


urlpatterns = [
    # manage:
    path('', manage_list, name='manage_list'), 

    # carousel:
    path('carousel/list/', carousel_list, name='carousel_list'), 
    path('carousel/create/', carousel_create, name='carousel_create'), 
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'), 

    # page:
    path('page/list/', page_list, name='page_list'), 
    path('page/create/', page_create, name='page_create'), 
    path('page/update/<int:pk>/', page_update, name='page_update'), 
    path('page/delete/<int:pk>/', page_delete, name='page_delete'), 
] 