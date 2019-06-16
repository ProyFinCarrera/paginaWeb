import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server
import cv2
from PIL import Image
from io import BytesIO

import os
import time
import numpy
import base64
from picamera.array import PiRGBArray
from picamera import PiCamera
PAGE="""\
<html>
<head>
<title>picamera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""
class StreamingOutput(object):
    def __init__(self, camera):
        self.frame = None
        self.camera = camera
        self.buffer = io.BytesIO()
        self.condition = Condition()
    
    def set_red(self):
        camera.annotate_background = picamera.Color('red')
    
    def set_green(self):
        camera.annotate_background = picamera.Color('green')
        
    def set_name(self, name):
        self.camera.annotate_text = name

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
                self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                        img = Image.open(BytesIO(frame))
                        t_img= numpy.array(img)
                        (resul, face_resize , pos_face) = det_face.detect(t_img)          
                        output.set_name("No detecto")
                        output.set_red()
                        if resul:
                            print("vamos")
                            output.set_name("Detecto Rostro")
                            output.set_green()
                            print(type(frame))
                      
                        # saveSystem.save_img2(a)
                        # t2 = threading.Thread(target=saveSystem.save_img, args=(a,))
                        # t2.start()    
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True