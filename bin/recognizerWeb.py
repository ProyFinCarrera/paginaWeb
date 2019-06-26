import io
import picamera
import logging
import json
import socketserver
import threading
from threading import Condition
from threading import Thread
from http import server
import cv2
from PIL import Image
from io import BytesIO
import os
import time
import numpy
import base64
import sys
import psutil
from myfirebase import myfirebase
from footprint import footprint
from picamera.array import PiRGBArray
from picamera import PiCamera
import subprocess
from recognizerVideo import recognizerVideo
from recognizerVideo.faceDetector import faceDetector
from recognizerVideo.saveSystem import saveSystem
import http.client

PATH_DIR = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
PID = str(os.getpid())
PID_FILE = os.path.join(os.path.join(PATH_DIR, "tmp"), "mydaemon.PID")
PID_PROCESS = os.path.join(os.path.join(PATH_DIR, "tmp"), "process.PID")
FILE_FIN = os.path.join(os.path.join(PATH_DIR, "tmp"), "fin.PID")
FILE_PASS = os.path.join(os.path.join(PATH_DIR, "tmp"), "pass.PID")
FILE_REC = os.path.join(os.path.join(PATH_DIR,'tmp'),"recognizer.info")
WAIT = 50
flag_detect = True
flag_cont = 0 
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
                self.buffer.seek(0)
                self.condition.notify_all()
        return self.buffer.write(buf)

class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
                
    def do_GET(self):
        if self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                global flag_detect
                global flag_cont
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                        if flag_detect:
                            img = Image.open(BytesIO(frame))
                            t_img = numpy.array(img)
                            #rt_v = False
                            #name_img=""
                            #rt_v, name_img = det_video.only_video_img(t_img)
                            t1 = threading.Thread(target=det_video.only_video_img,
                                                args=(t_img,))
                            t1.start()
                            #t1.join()
                            if(flag_cont == WAIT):
                                output.set_name("Not detected")
                                output.set_red()
                            else:
                                if flag_cont < WAIT:
                                    flag_cont+=1                           
                        else:
                          if os.path.isfile(FILE_FIN):
                            os.unlink(FILE_FIN)
                            flag_cont = 0
                            if os.path.isfile(FILE_PASS):
                                os.unlink(FILE_PASS)
                                output.set_name("Correct Identification")
                                output.set_green()
                            else:
                                output.set_name("Identification error")
                                output.set_red()
                                det_video.active_cont()
                            flag_detect = True
                            
                        if os.path.isfile(FILE_REC):
                            name = open(FILE_REC, "r").read()
                            only_name = name.split("_")
                            output.set_name("Detect:" + str(only_name[0]))
                            output.set_green()
                            os.unlink(FILE_REC)
                            aux  = os.path.join(PATH_DIR ,'mainVerifyFootprint.py')
                            cmd = ['python', aux , name]
                            p = subprocess.Popen(cmd)
                            flag_detect = False
                            # open(PID_PROCESS, "w").write(str(p.pid))
                            print("Activo suproceso")
                            det_video.cancel_cont()
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
        #raise ValueError('The program is in process')
    else:
        open(PID_FILE, "w").write(PID)
    
    det_face = faceDetector.FaceDetector()
    det_video = recognizerVideo.RecognizerVideo(
    maxiR=3, selRecon=1)
        #det_footprint = footprint.Footprint()
        #db = myfirebase.MyFirebase()
    print("ussss")
    with picamera.PiCamera(resolution='640x480', framerate=30) as camera:
         output = StreamingOutput(camera=camera)
         camera.hflip=True
         camera.annotate_text = "Not detected"
         camera.annotate_background = picamera.Color('red')
         camera.start_recording(output, format='mjpeg',quality=30)
         try:
            address = ('127.0.0.1', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
         finally:
               camera.stop_recording()
except Exception as e:
    print('Exception message: ' + str(e))


