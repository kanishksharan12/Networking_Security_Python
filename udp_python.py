#!/usr/bin/python
__author__ = 'Kanishk Sharan'

import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(b"Hi, this is a message", ("172.30.42.117", 5599))
    print("Sent the message")
except Exception as e:
    print("Exception: ", e)
finally:
    print("Done")