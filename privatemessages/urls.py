from django.conf.urls import  url
from django.urls import path,include
from privatemessages.views import *



urlpatterns =[
    url(r'^send_message/$', send_message_view),
    url(r'^send_message_api/(?P<thread_id>\d+)/$', send_message_api_view),
    url(r'^chat/(?P<thread_id>\d+)/$', chat_view),
    url(r'^$', messages_view),
    path('register/',register,name="register"),
    path('logout/', logout_view, name="logout"),
    path('home',)




]
