from django.shortcuts import render

from datetime import date


def home(request):
    context = {
        "first_name": 'Name_from_View',
        "last_name": 'Last_name_from_View',
        "date_of_birth": date.today(),
        "bio": 'Bio test from view',
        "email": 'test_view@exampl.com',
        "jid": 'jid_test_view@exampl.com',
        "skype": 'skype_id',
        "other": 'Other contacts from view'
    }
    return render(request, 'hello/home.html', context)
