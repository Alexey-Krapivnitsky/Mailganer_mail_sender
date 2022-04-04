from django.conf.urls import url, include

from sender.views import HomeView, CreateMailing, OwnerMailing, \
    DeleteMailing, SendMailing, CheckOpenMailing

app_name = 'sender'

urlpatterns = [
    url(r'^home/', HomeView.as_view(), name="home"),
    url(r'^mail/create/', CreateMailing.as_view(), name='create_mail'),
    url(r'^mail/all/', OwnerMailing.as_view(), name='all_mail'),
    url(r'^mail/delete/(?P<pk>[\w]+)/$', DeleteMailing.as_view(), name='delete'),
    url(r'^mail/send/(?P<pk>[\w]+)/$', SendMailing.as_view(), name='send'),
    url(r'^mail/open/(?P<pk>[\w]+)/$', CheckOpenMailing.as_view(), name='check_open'),
    url(r'^mail/open/(?P<pk>[\w]+)/(?P<link>[\w]+)/$', CheckOpenMailing.as_view(), name='check_open_link'),
]
