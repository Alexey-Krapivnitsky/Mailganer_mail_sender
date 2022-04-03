# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, View
from django.views.generic.detail import SingleObjectTemplateResponseMixin

from accounts.forms import LoginForm
from accounts.models import UserAccount


class SignUp(CreateView):
    account_fields = ['birthday', 'state']
    form_class = LoginForm
    success_url = reverse_lazy('accounts:account')
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        account_data = {key: request.POST[key] for key in self.account_fields}
        form = self.get_form()

        if form.is_valid():
            self.form_valid(form)
            user = form.instance
            user.password = make_password(request.POST.get('password'))
            user.save()
            account_data.update({'user': user})
            UserAccount.objects.create(**account_data)
            login(self.request, user)

            return HttpResponseRedirect(redirect_to=self.success_url)
        else:
            return self.form_invalid(form)


class AccountView(SingleObjectTemplateResponseMixin, View):
    queryset = UserAccount.objects.all()
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        account = self.queryset.get(user=self.request.user)
        community = self.queryset.filter(state='o') if account.state == 's' else\
            self.queryset.filter(state='s')
        owner_community = community.filter(user=request.user)
        context = {
            'account': account,
            'community': community,
            'my_community': owner_community
        }
        return self.render_to_response(context)
