from django.contrib import admin
from django.urls import include, path # 追加部分
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('line_bot_ai/', include('line_bot_ai.urls')), # 追加部分
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 追加部分