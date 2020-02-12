from django.shortcuts import render


def specific_secret(request, uid=None):
    return render(request, 'secret.html', {'uid': uid})
