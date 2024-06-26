from django.http import HttpResponseRedirect


def index(request):
    print('-----------------------------TESTE PRE-COMMIT-------------------------------- ')
    return HttpResponseRedirect('/backoffice/')
