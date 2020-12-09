from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import login as login, authenticate, logout as logout
from django.utils.safestring import mark_safe
import json



# Create your views here.
def home(request):
    return render(request, 'index.html')