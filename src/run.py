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
client.clear()
client.consume(1)
client.random(1)
client.add(uri)
client.play()
time.sleep(5)
print(client.currentsong())
for x in range(1, 10):
    client.next()
    time.sleep(0.2)
    print(client.currentsong())
    time.sleep(5)

client.stop()
client.disconnect()
