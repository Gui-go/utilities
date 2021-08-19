#!/bin/python3

# https://www.oreilly.com/library/view/python-standard-library/0596000960/ch07s20.html
# 1:18:00 https://www.youtube.com/watch?v=lZAoFs75_cs&t=2s


import http.server
import socketserver

# Minimal web server.  
# Serves files relative to the current directory.

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"serving at port", PORT)
httpd.serve_forever()
