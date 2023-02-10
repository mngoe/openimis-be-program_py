from io import TextIOWrapper
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _
from django.http.response import JsonResponse
from django import utils
import logging
import pandas as pd

logger = logging.getLogger(__name__)
