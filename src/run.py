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
uri = 'spotify:track:30sHxvIflGaWj7nnd3oSTo'

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
client.consume(1)
client.random(1)
# client.crossfade(2)
client.add(uri)
client.play()
time.sleep(3)
client.next()
time.sleep(3)
client.next()
time.sleep(3)
client.next()
time.sleep(3)
client.stop()
client.disconnect()
