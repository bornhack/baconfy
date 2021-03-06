#!/usr/bin/env python3

# IMPORTS
from mpd import (MPDClient, CommandError)
from socket import error as SocketError
from sys import exit
import time

## SETTINGS
##
HOST = 'localhost'
PORT = '6600'
PASSWORD = "password"
###
# Chill test sounds
# uri = 'spotify:user:b584371:playlist:4zlvIZSMVmeb0N6ZgLU7sk'
uri = 'spotify:user:b584371:playlist:06nxCXR3zlRAxwqAz6FfaD'

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
client.clear()
client.random(1)
client.add(uri)
client.consume(0)
# client.crossfade(3)
# print(client.playlist())
client.play()
time.sleep(5)
'''
print(client.currentsong())
for x in range(1, 10):
    client.next()
    time.sleep(0.2)
    print(client.currentsong())
    time.sleep(5)
'''

while True:
    try:
        print(client.currentsong())
        time.sleep(3)
    except KeyboardInterrupt:
        print('Terminated by CTRL-C')
        # logging.info('Terminated by CTRL-C')
        break

client.stop()
client.disconnect()
