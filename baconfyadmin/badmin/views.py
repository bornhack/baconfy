from django.http import HttpResponse
from . import baconfy


def index(request):

    client = baconfy.baconfyclient()
    songInfo = client.currentsong()
    return HttpResponse(songInfo)
