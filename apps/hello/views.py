from django.shortcuts import render

from apps.hello.models import Person


def home(request):
    p = Person.objects.all().first()
    context = {}
    if p:
        context = {
            "first_name": p.first_name,
            "last_name": p.last_name,
            "date_of_birth": p.date_of_birth,
            "bio": p.bio,
            "email": p.email,
            "jid": p.jid,
            "skype": p.skype,
            "other": p.other
        }
    return render(request, 'hello/home.html', context)
