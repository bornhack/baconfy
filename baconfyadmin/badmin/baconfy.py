#!/usr/bin/env python3

# IMPORTS
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
from sys import exit
import time
import json
import pprint
# import datetime
# import time
# SETTINGS
#
HOST = 'localhost'
PORT = '6600'
PASSWORD = "password"


class baconfyclient(object):
    """docstring for  baconfyclient"""
    def __init__(self):
        super(baconfyclient, self).__init__()
        # self.arg = arg
        self.connect()

    def play(self):
        self.client.play()

    def chunks(self, l, n):
        n = max(1, n)
        return [l[i:i + n] for i in range(0, len(l), n)]

    def pause(self):
        self.client.pause()

    def prev(self):
        self.client.previous()

    def init1337(self):
        self.connect()
        self.client.clear()
        self.client.add('spotify:user:b584371:playlist:4PaYAhJ2xibbm5q69yXgI7')
        #self.client.add('spotify:user:b584371:playlist:06nxCXR3zlRAxwqAz6FfaD')

    def playlist(self):
        playlist = self.client.playlist()
        playlistd = self.chunks(playlist,11)
        #pprint.pprint(playlistd)
        playlistan = {}
        for lista in playlistd:
            #print(lista)
            playlistan[str(lista[0]).strip(' ')] = {
                'file': str(lista[0]).strip(' '),
                'time': int(str(lista[1]).strip(' ')),
                'artist': str(lista[2]).strip(' '),
                'album': str(lista[3]).strip(' '),
                'title': str(lista[4]).strip(' '),
                'date': int(str(lista[5]).strip(' ')),
                'track': str(lista[6]).strip(' '),
                'pos': int(str(lista[7]).strip(' ')),
                'id': int(str(lista[8]).strip(' ')),
                'albumartist': str(lista[9]).strip(' '),
                'x-albumuri': str(lista[10]).strip(' '),
            }
            #print(type(lista))
            # file, time, artist, album, title, date, track, ppos, pid, albumartist, albumuri = map(lambda x: 11, lista)
            #print(map(lambda x: 11, lista))
        # pprint.pprint(playlistan)
        # print(json.dumps(playlist))
        return(playlistan)

    def next(self):
        self.client.next()

    def seek(self):
        return self.client.status()

    def status(self):
        return self.client.status()

    def percentage(self, part, whole):
        return 100 * float(part)/float(whole)

    def connect(self):
        self.client = MPDClient()

        try:
            self.client.connect(host=HOST, port=PORT)
        except SocketError:
            exit(1)

        if PASSWORD:
            try:
                self.client.password(PASSWORD)
            except CommandError:
                exit(1)
        self.client.consume(0)
        self.client.random(1)

    def sec2min(self, seconds):
        res = time.strftime('%M:%S', time.gmtime(int(seconds)))
        return res

    def currentsong(self):
        # print('test')
        songInfo = self.client.currentsong()
        status = self.client.status()
        # print(type(songInfo))
        # print(songInfo['time'])
        # return('Currently Playing: %s - %s [%s] (%s)' % (
        #     songInfo['artist'],
        #     songInfo['title'],
        #     self.sec2min(songInfo['time']),
        #     songInfo['album']
        # ))
        return {'song': songInfo, 'status': status}

    def nextsong(self):
        self.client.next()
        time.sleep(0.2)
