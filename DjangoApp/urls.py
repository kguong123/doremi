from datetime import datetime
from .views import HomeView
from .views import UserCreateView, UserCreateDoneTV

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next lines to enable the admin:

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', HomeView, name='home'),  
    url(r'^recipe/', include('recipe.urls', namespace='recipe')),
    url(r'^honeytip/', include('honeytip.urls', namespace='honeytip')),
    url(r'^delivery/', include('delivery.urls', namespace='delivery')),
    url(r'^randomcooking/', include('randomcooking.urls', namespace='randomcooking')),
    url(r'^mypage/', include('mypage.urls', namespace='mypage')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
