# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, View
from django.utils.translation import ugettext as _

from sender.forms import MailingForm
from sender.models import Mailing
from sender.tasks import send_mailing


class InitialView(TemplateView):
    template_name = 'index.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class CreateMailing(CreateView):
    form_class = MailingForm
    success_url = reverse_lazy('accounts:account')
    queryset = Mailing.objects.all()
    template_name = 'create_mail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=request.user)
        context = {'form': form}
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(user=request.user, data=request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user
            saving.save()
            return HttpResponseRedirect(redirect_to=self.success_url)
        else:
            self.object = None
            return self.form_invalid(form)


class OwnerMailing(ListView):
    queryset = Mailing.objects.all()
    template_name = 'all_owner_mail.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset().filter(user=request.user)
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


class DeleteMailing(DeleteView):
    model = Mailing
    success_url = reverse_lazy('sender:all_mail')
    template_name = 'mailing_confirm_delete.html'


class SendMailing(View):
    success_url = reverse_lazy('sender:all_mail')

    def get(self, request, *args, **kwargs):
        parameters = {
            'owner': request.user.pk,
            'mailing': kwargs.get('pk')
        }
        send_mailing.delay(parameters)
        return HttpResponseRedirect(redirect_to=self.success_url)
