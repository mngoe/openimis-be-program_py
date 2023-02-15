""" Model OpenIMIS Be Cheque Santé
Models of Cameroon Cheque Santé project
"""
import datetime
from dataclasses import dataclass

from django.core.exceptions import ValidationError
from django.db import models
from core import models as core_models
from core.models import InteractiveUser
from django.http import request
from django.utils import timezone as django_tz 
import pandas as pd
import logging

logger = logging.getLogger(__name__)
class Program(models.Model):
    """ Class Program :
    Class for importation of check in the system
    """
    idProgram = models.AutoField(
        primary_key=True
    )
    nameProgram = models.CharField(db_column='Name', max_length=248)
    validityDate = models.DateTimeField(
        'Program Validity Date', 
        default=django_tz.now,
        blank=True,
        null=True
    )
    user = models.ManyToManyField(InteractiveUser)

    """ Class Meta :
    Class Meta to define specific table
    """

    class Meta:
        db_table = "tblProgram"