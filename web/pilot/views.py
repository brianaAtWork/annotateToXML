from django.shortcuts import render
from pilot.models import *
from pilot.forms import forms

def main(request):
    return render(request, "noaa_test.html")

def form(request):
    model_name = request.GET.get("model")
    form = forms[model_name]

    return render(request, "form.html", {
        "form": form
    })
