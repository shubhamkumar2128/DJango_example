from django.shortcuts import render

from .models import Dest


def index(request):
    dest1 = Dest()
    dest1.name = "UP"
    dest1.desc = "Uttar Pradesh"
    dest1.price = 324
    dest1.offer = True

    dest2 = Dest()
    dest2.name = "UP"
    dest2.desc = "Uttar Pradesh"
    dest2.price = 727
    dest2.offer = True

    dest3 = Dest()
    dest3.name = "UP"
    dest3.desc = "Uttar Pradesh"
    dest3.price = 628
    dest3.offer = False

    dest4 = Dest()
    dest4.name = "UP"
    dest4.desc = "Uttar Pradesh"
    dest4.price = 527
    dest4.offer = False

    dest5 = Dest()
    dest5.name = "UP"
    dest5.desc = "Uttar Pradesh"
    dest5.price = 227
    dest5.offer = True

    dest6 = Dest()
    dest6.name = "UP"
    dest6.desc = "Uttar Pradesh"
    dest6.price = 227
    dest6.offer = True

    dests = [dest1, dest2, dest3, dest4, dest5,dest6]

    return render(request, "index.html", {'dests': dests})
