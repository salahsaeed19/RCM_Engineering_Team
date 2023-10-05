from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('authentication.urls')),
    path('blog/', include('blog.urls')),
    path('', include('ourteam.urls')),
    path('summaries/', include('engineering_summaries.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'main.views.custom_500'
handler404 = 'main.views.custom_404'