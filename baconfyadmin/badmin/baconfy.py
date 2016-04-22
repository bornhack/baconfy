#!/usr/bin/env python3

# IMPORTS
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
from sys import exit
import time
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

    def sec2min(self, seconds):
        res = time.strftime('%M:%S', time.gmtime(int(seconds)))
        return res

    def currentsong(self):
        print('test')

        songInfo = self.client.currentsong()
        # print(type(songInfo))
        # print(songInfo['time'])
        return('Currently Playing: %s - %s [%s] (%s)' % (
            songInfo['artist'],
            songInfo['title'],
            self.sec2min(songInfo['time']),
            songInfo['album']
        ))

    def nextsong(self):
        self.client.next()
        time.sleep(0.2)
