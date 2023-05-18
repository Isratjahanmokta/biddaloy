from django.contrib import admin
from django.urls import path, include
from authentication.views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('authentication.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
