#!/usr/bin/env python

import sys
import socket
import time
import re
import os
import threading
import time
import subprocess

from threading import Thread
from voice_client import handle_audio_input


#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8999        # Port to listen on (non-privileged ports are > 1023)
BUFF_SIZE = 1 
MIN_VALUE = 3

#Sending lex_response to client for TTS
def send_to_client(response):
    if(response.find('value') != -1):
        tmp = response.rsplit(',')[0]
    else:
        tmp = response
    conn.send(str(len(tmp)).encode())
    conn.send("\n".encode())
    conn.send(tmp.encode())

#Sending lex_response to process the navigation request
def sendGoal(response):
    if(response.find('value') != -1):
        tmp = response.replace(" ", "")
        os.system('%s %s' % ('python hometour.py', tmp))


#Server connection to with Client
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', PORT))
        s.listen(10)
        print("\n Server is listening on port :", PORT, "\n")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                print("Ready to receive audio")
		#Recieving audio file from android client
                RecvData = conn.recv(10).decode('utf-8', 'replace')
                sizeOfData = re.sub("\D", "", RecvData)
                while len(sizeOfData) < MIN_VALUE: 
                    RecvData = conn.recv(10).decode('utf-8', 'replace')
                    sizeOfData = re.sub("\D", "", RecvData)
                n = int(sizeOfData)
                data = b''
                print("Recieved request")
                while len(data) < n:
                    if((n-len(data)) > MIN_VALUE):
                        data += conn.recv(BUFF_SIZE)
                    else:
                        break
		# sending audio data to lex
                response = handle_audio_input(data)
		# Send goals asynchronously to navigation stack
                thread = threading.Thread(
                    target=sendGoal, args=(response,))
                thread.daemon = True
                thread.start()
                send_to_client(response)
