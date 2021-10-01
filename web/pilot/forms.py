from django.forms import modelform_factory

import inspect

import pilot.models

forms = {}

for n,c in inspect.getmembers(pilot.models):
    if inspect.isclass(c) and c.__module__ == "pilot.models" and not c._meta.abstract:
        forms[n] = modelform_factory(c, fields="__all__")
