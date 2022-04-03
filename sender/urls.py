from django.conf.urls import url, include

from sender.views import HomeView, CreateMailing, OwnerMailing, DeleteMailing, SendMailing

app_name = 'sender'

urlpatterns = [
    url(r'^home/', HomeView.as_view(), name="home"),
    url(r'^mail/create/', CreateMailing.as_view(), name='create_mail'),
    url(r'^mail/all/', OwnerMailing.as_view(), name='all_mail'),
    url(r'^mail/delete/(?P<pk>[\w]+)/$', DeleteMailing.as_view(), name='delete'),
    url(r'^mail/send/(?P<pk>[\w]+)/$', SendMailing.as_view(), name='send'),
]
