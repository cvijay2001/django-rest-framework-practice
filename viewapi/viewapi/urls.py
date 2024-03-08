
from django.contrib import admin
from django.urls import path,include
# from viewapi_app import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('viewapi_app.urls'))
]
