# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import CASCADE
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Mailing(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=50, verbose_name='Тема сообщения')
    body = RichTextUploadingField(verbose_name="Текст сообщения")

    def __str__(self):
        return self.title
