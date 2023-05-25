
from django.contrib import admin
from django.urls import path
from service.views import available_dates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', available_dates, name='available_dates'),
]

