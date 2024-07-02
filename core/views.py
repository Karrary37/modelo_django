from django.http import HttpResponseRedirect


def index():
    print('-------------------------------------- Teste Pre-commit ------------------------------------')
    return HttpResponseRedirect('/backoffice/')
