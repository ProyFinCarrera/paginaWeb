import io
import picamera
import logging
import json
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
import sys
from myfirebase import myfirebase
from footprint import footprint
from picamera.array import PiRGBArray
from picamera import PiCamera
from recognizerVideo.faceDetector import faceDetector
from recognizerVideo.saveSystem import saveSystem

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")

class StreamingOutput(object):
    def __init__(self, camera):
        self.frame = None
        self.camera = camera
        self.buffer = io.BytesIO()
        self.condition = Condition()
    
    def get_photo(self):
        return self.photos
    
    def set_photo(self, photos):
        self.photos = photos
    
    def set_red(self):
        camera.annotate_background = picamera.Color('red')
    
    def set_green(self):
        camera.annotate_background = picamera.Color('green')
        
    def set_name(self, name):
        self.camera.annotate_text =name

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
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        
    def do_POST(self):
        path = self.path.split("?")
        print( path)
        if path[0] == '/footprintSave':
            try:
                #print(self)
                check , vec_aux = det_footprint.save_footprint();
                #print(vec_aux)
                content = json.dumps({'code':0,'message':'All right'}).encode('utf-8')
                if vec_aux == 2:
                    content = json.dumps({'code':2,'message':'Footprint not registered'}).encode('utf-8')
                elif vec_aux == 3:
                    content = json.dumps({'code':3,'message':'Footprint is in the system'}).encode('utf-8') 
                
                self.do_OPTIONS()
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', len(content))
                self.end_headers()
                self.wfile.write(content)
                #email  = sys.argv[1]
                email = path[1]# "perez@gmail.com"
                print(check)
                if check:              
                   ok = db.upload_footprint(vec_aux, email)
                   if ok:
                       print("Save footprint ok")
                #det_footprint = footprint.Footprint()
                
            except Exception as e:
                 logging.warning('Warrning: %s', str(e))
                 self.send_error(404)
                 self.end_headers()
                 
        
    def do_GET(self):
        if self.path == '/stream.mjpg':
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
                        output.set_name("Not detected")
                        output.set_red()
                        if resul:
                            output.set_name("Detect Face")
                            output.set_green()
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
    
try:
    if os.path.isfile(PID_FILE):
        print("%s the file exist" % PID_FILE)
        raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)  
        det_face = faceDetector.FaceDetector(save_face=True)
        det_footprint = footprint.Footprint()
        db = myfirebase.MyFirebase()
        with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
            output = StreamingOutput(camera=camera)
            camera.hflip=True
            camera.annotate_text = "Not detected"
            camera.annotate_background = picamera.Color('red')
            camera.start_recording(output, format='mjpeg')
            try:
                address = ('127.0.0.1', 8000)
                server = StreamingServer(address, StreamingHandler)
                server.serve_forever()
            finally:
                camera.stop_recording()
except Exception as e:
    print('Exception message: ' + str(e))
