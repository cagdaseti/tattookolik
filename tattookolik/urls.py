from django.contrib import admin
from django.urls import path, include
from page.views import index,about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name="about"),
    path('manage/', include('page.urls'), ),
    path('user/', include('user.urls'), ),
    path('articles/', include("article.urls")),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)

urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT)