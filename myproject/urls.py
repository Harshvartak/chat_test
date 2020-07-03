from django.conf.urls import  include, url
from django.urls import path, include

from django.contrib import admin

urlpatterns =[
        url(r'^messages/', include('privatemessages.urls')),
        url(r'^admin/', admin.site.urls),

]
