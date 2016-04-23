from . import baconfy
from .forms import NameForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
import pprint


def index(request):
    # print(request)
    client = baconfy.baconfyclient()
    songInfo = client.currentsong()
    return HttpResponse(songInfo)
    # return HttpResponse(songInfo)


def actionhandler2(request, action):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def actionhandler(request, action):
    client = baconfy.baconfyclient()
    if action == 'playing':
        songInfo = client.currentsong()
        return render(request, 'play.html', {
            'data': songInfo,
            'playPercentage': 100 * float(songInfo['status']['elapsed'])/float(songInfo['song']['time']),
            'played': client.sec2min(int(round(float(songInfo['status']['elapsed'])))),
            'songtime': client.sec2min(songInfo['song']['time']),
        })
    elif action == 'play':
        client.play()
        return HttpResponseRedirect('/badmin/playing')
    elif action == 'next':
        client.next()
        return HttpResponseRedirect('/badmin/playing')
    elif action == 'prev':
        client.prev()
        return HttpResponseRedirect('/badmin/playing')
    elif action == 'pause':
        client.pause()
        return HttpResponseRedirect('/badmin/playing')
    elif action == 'progress':
        songInfo = client.currentsong()
        res = round(100 * float(songInfo['status']['elapsed'])/float(songInfo['song']['time']),0)
        return HttpResponse(json.dumps({
                'song': songInfo['song'],
                'status': songInfo['status'],
                'percentage': res,
            }))
        #return HttpResponse('60')
    else:
        return HttpResponse('Unknown action')
    # return HttpResponse(client.currentsong())
