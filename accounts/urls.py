from django.conf.urls import url, include

from accounts.views import SignUp, AccountView

app_name = 'accounts'

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url(r'^signup/', SignUp.as_view(), name='signup'),
    url(r'^account', AccountView.as_view(), name='account')
]
