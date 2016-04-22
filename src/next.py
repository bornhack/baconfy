#!/usr/bin/env python3

# IMPORTS
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
from sys import exit
import time
# import datetime
# import time


def sec2min(seconds):
    res = time.strftime('%M:%S', time.gmtime(int(seconds)))
    return res

# SETTINGS
#
HOST = 'localhost'
PORT = '6600'
PASSWORD = "password"
#
# Chill test sounds
uri = 'spotify:user:b584371:playlist:4zlvIZSMVmeb0N6ZgLU7sk'

client = MPDClient()

try:
    client.connect(host=HOST, port=PORT)
except SocketError:
    exit(1)

if PASSWORD:
    try:
        client.password(PASSWORD)
    except CommandError:
        exit(1)

client.next()
time.sleep(0.2)
songInfo = client.currentsong()
# print(type(songInfo))
# print(songInfo['time'])
print('Currently Playing: %s - %s [%s] (%s)' % (
    songInfo['artist'],
    songInfo['title'],
    sec2min(songInfo['time']),
    songInfo['album']
))
client.disconnect()
