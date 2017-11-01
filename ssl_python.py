#!/usr/bin/python3
__author__ = 'Kanishk Sharan'

import ssl
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock = ssl.wrap_socket(s)

try:
    ssock.connect(("www.bbc.com", 443))
    print(ssock.cipher())
except:
    print("error")

try:
    ssock.write(b"GET / HTTP/1.1 \r\n")
    ssock.write(b"Host: www.bbc.com\n\n")
except Exception as e:
    print("write error: ", e)

data = bytearray()
try:
    data = ssock.read()
except Exception as e:
    print("read error: ", e)

print(data.decode("utf-8"))
