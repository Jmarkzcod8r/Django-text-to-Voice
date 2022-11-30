from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index_page, name="index"),
    path('about', views.about_page, name="about"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
