from . import baconfy
from .forms import NameForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


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
        client.play()
        songInfo = client.currentsong()
        return render(request, 'play.html', {'msg': songInfo})
    elif action == 'next':
        client.next()
        return HttpResponseRedirect('/badmin/playing')
    else:
        return HttpResponse('Unknown action')
    # return HttpResponse(client.currentsong())
