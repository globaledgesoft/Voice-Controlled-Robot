#!/usr/bin/env python

import subprocess
import os
import sys

# Recieved lex_response from server.
lex_response=sys.argv[1]

# Assigning place_value based on lex_response (kitchen,hall,room,outdoor,stop,previous)
if(lex_response.find("0") != -1):
  place = "STOP"
  place_value = 0
  os.system("python3 stop.py")
elif(lex_response.find("1") != -1):
  place = "KITCHEN"
  place_value = 1
elif(lex_response.find("2") != -1):
  place = "HALL"
  place_value = 2
elif(lex_response.find("3") != -1):
  place = "ROOM"
  place_value = 3
elif(lex_response.find("4") != -1):
  place = "PARKING"
  place_value = 4
elif(lex_response.find("5") != -1):
  place = "OUTDOOR"
  place_value = 5
elif(lex_response.find("6") != -1):
  place = "PREVIOUS"
  place_value = 6
  os.system("python3 stop.py")
else:
  place_value = 7

if place_value == 0:
  print(place_value)
elif place_value != 0 & place_value != 7 :
  # Assigning navigation goals based on place_value for all requests, except STOP
  os.system('%s %s' % ("python set_goal.py",place))
else:
  print (lex_response)

