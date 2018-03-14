from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('Posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include('Posts.urls')),
]
