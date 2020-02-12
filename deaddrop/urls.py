from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .web.views import specific_secret
from .api.urls import router

admin.autodiscover()

urlpatterns = [
    # url(r'', TemplateView.as_view(template_name="base.html"), name='index'),
    url(r'secret/(?P<uid>\w+)/?', specific_secret, name='detail'),
    url(r'api/v1/', include(router.urls)),
    url(r'admin-panel/?', admin.site.urls),
    url(r'', TemplateView.as_view(template_name="base.html"), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
