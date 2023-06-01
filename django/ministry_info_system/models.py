import json
import datetime
from tempfile import template

from django.db import models
from django.contrib.postgres import fields

from django.utils.translation import gettext_lazy as _
from django.forms.models import model_to_dict
from django.utils.html import format_html, mark_safe

from django.conf import settings

import uuid

from simple_history.models import HistoricalRecords
from django.core.validators import FileExtensionValidator

class MedicalEnsuranceType(models.TextChoices):
    GENERAL = 'GENERAL', _('Загальний') 
    VIP = 'VIP', _('Особливий') 
    LIMITED = 'LIMITED', _('Обмежений')


class MedicalEnsurance(models.Model):
    id = models.AutoField(primary_key=True)

    ensurance_type = models.CharField(max_length=20, choices=MedicalEnsuranceType.choices, 
                                                    default=MedicalEnsuranceType.GENERAL,
                                                    verbose_name='Тип медичного страхування')

    person_unique_code = models.CharField(max_length=10, null=True, blank=True, unique=True,
                                       verbose_name='Код РНОКПП особи', help_text='Подається разом з заявою')

    person_fullname = models.CharField(max_length=255, null=True, blank=True,
             verbose_name='Повне ім\'я особи', help_text='Вноситься вручну')
    person_home_address = models.CharField(max_length=512, null=True, blank=True,
             verbose_name='Домашня адреса', help_text='Вноситься вручну')
    person_medical_ensurance = models.CharField(max_length=512, null=True, blank=True,
             verbose_name='Номер та дата медичного страхування', help_text='Вноситься вручну')
    

    created_at = models.DateTimeField(verbose_name='Дата створення запису', auto_now_add=True,)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення інформації про запис', auto_now=True,)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Медичне страхування'
        verbose_name_plural = 'База медичного страхування'

    # def __str__(self):
    #     return self.сertificate_no + " " + self.applicant_fullname