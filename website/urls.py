from django.contrib import admin
from django.urls import path, include
from django.conf import settings as st
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve 

#this just changes the django admin header
admin.site.site_header = "SIP WEBSITE ADMIN"
admin.site.site_title = "SIP WEBSITE ADMIN"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('materials/', include('materials.urls')),
    path(r'^download/(?P<path>.*)$' , serve,{'document_root':st.MEDIA_ROOT}),
]

urlpatterns += static(st.STATIC_URL, document_root=st.STATIC_ROOT)
    
    
