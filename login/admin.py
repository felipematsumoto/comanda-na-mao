# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import TipoConta, Usuario

admin.site.register(TipoConta)
admin.site.register(Usuario)
