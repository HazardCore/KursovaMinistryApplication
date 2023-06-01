import datetime

from django.contrib import admin

from ministry_info_system.models import *

import os
import uuid
import datetime
import simple_history
from import_export.admin import ExportActionMixin

from dateutil.relativedelta import relativedelta

from django.contrib import admin, messages
from django.utils.html import format_html, mark_safe
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.forms import *
from django.http import HttpResponseRedirect

from django.core.files import File

import requests

from rangefilter.filters import DateRangeFilter

from django_tabbed_changeform_admin.admin import DjangoTabbedChangeformAdmin

from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter

from django.contrib.auth.models import Group, Permission

# ------------------------------ MODEL ------------------------------ #

class RemoveAdminDefaultMessageMixin:

    def remove_default_message(self, request):
        storage = messages.get_messages(request)
        try:
            del storage._queued_messages[-1]
        except KeyError:
            pass
        return True

    def response_add(self, request, obj, post_url_continue=None):
        """override"""
        response = super().response_add(request, obj, post_url_continue)
        self.remove_default_message(request)
        return HttpResponseRedirect('../')
        # return response

    def response_change(self, request, obj):
        """override"""
        response = super().response_change(request, obj)
        self.remove_default_message(request)
        return response

    def response_delete(self, request, obj_display, obj_id):
        """override"""
        response = super().response_delete(request, obj_display, obj_id)
        self.remove_default_message(request)
        return response


class MedicalEnsuranceAdmin(DjangoTabbedChangeformAdmin, RemoveAdminDefaultMessageMixin, ExportActionMixin):
    # PERMISSIONS
    def has_add_permission(self, request, obj=None): 
        return True

    def has_change_permission(self, request, obj=None): 
        return True

    def has_delete_permission(self, request, obj=None): return True


    def get_readonly_fields(self, request, obj=None):
        readfields = ['id', 'created_at', 'updated_at',]
        return readfields


    fieldsets = [
        (None, {'fields': [
            'id',
            'ensurance_type',
            'person_unique_code',
            'person_fullname',
            'person_home_address',
            'person_medical_ensurance',
            'created_at',
            'updated_at',
        ],
        "classes": ["tab-detail"]}),
    ]

    tabs = [
        ("Деталі", ["tab-detail"]),
    ]
    
    list_display = ('id', 'ensurance_type', 'person_fullname',)
    list_filter = (
        'ensurance_type',
    )
    list_per_page = 40


admin.site.register(MedicalEnsurance, MedicalEnsuranceAdmin)


admin.site.index_title = "База даних міністерства"

