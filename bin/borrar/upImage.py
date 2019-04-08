#! /usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

##  databaseURL: 'https://tfg-findegrado.firebaseio.com'

conf = {
  "type": "service_account",
  "project_id": "tfg-findegrado",
  "private_key_id": "36962c4658e3d9b2661b78f9028481024a7c4060",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC125TQLCdJX2zI\nL720qeNQBjrX3lIzyGgULW6LHRTWEc4PVxAg6cBMK6SJt4XKNVD+/8llTbi1SK84\ngZf1NYhjBlDUUQKzs3EvIPFlY6ceXPsVV7t18QOoxfEOxMAe1TpXZrnkdL2TZdbT\n1u420XCf3f8mrI17BQNMVvhUTEGVF+FRwXs7Mz956Bp0XOhazKBPhcAfQCweknaA\nTtc88YkGr2icgz4UYGB4QrTSiEmSnUWN7jVDhNakNrWrkRjszqSu4nv9Fj5iDJkW\neXout9BLD4mV/mNx/iOEjWQI5TfauVv/Xl/ocADKvwjPRlc+HIZSzeN89uNeB0fZ\n08Kg7jFNAgMBAAECggEABclNEJubC2ddIXh9Z4JxUGJGXIh/IpUplJzGc+gyucX6\nwbuyMG3nl7TaySP8/oxYPajbWl0Q97muk5RyBpQTuRziFQNX2+ple0unyqNTVbC9\nL3ZpaU0IIgZcT208tK5xqwbCeu2o+4flwDtKPJXI6NlKLUuXu9aSvorU32/GtWzt\nm3dIIwC5Y0pcsjATG6gi5ldCLLZg5itVEjsRrogWg958w7cWK7e89z3ccPsQcyL4\nz9pZGQCBFhU7U06vldkvAGrW8XbBnGuV+LL7hb7/2SvgKvay3PtyYcZ5WZRp/s5h\nAkeVivmSJw26ua1CSBNqu/iQN1nbflShBsjc/Ua+GQKBgQDb4NMqv7PGAjKZbabx\nGbcNtUpVHjOqS7JEfmfLYVkZOes2OiIYkn5Z/J4u4EMN+jCsJStIz+xO1h93niC3\n22IT2ZWf5XH+Eg2MrWmFDRgAUr5X9uRlok4JKLZEvIFti5jNq5iqUWVAyNPUnm4/\nKZfCjcKpVh7tJ5+nfd1tKbfmWQKBgQDTu8VjwKnfi+9UNcoYEOYdwwCEwhAVmUUE\n2iO0OG+E1Dlkau4Y2w29Eh1tItrVPpF/QCrSQlqNkHvsMVjSMZYzw20qIosbABTa\nWQwAdZBFUHeUCfyUTS3dIdHjqF8N9RfNAtOiblyHJqvaPqhICn0ddv0luLZncSob\nYeY3vSksFQKBgCeJ+U8ho+lCcejnL/MBJcrAQ/qkcLP54rewZ2fKPKRtpt9ces8i\nYLg71hIl38j+qYv7Lxpr0Vmn5Ya0F7wYJj3djatwLhx7EJawhF4Zqaw9NN9KlW21\nTwUUnhokL74MMVEiv1Q5SNTqiDUevEJ9bz3cEhozU2JgErSizJOZwekZAoGARiBo\nzhMfsESerdtq5fGi5bSSVWYZAa5T57mAHc6bUPkhURsBZQYYVMjNKjpjFEG22tib\n1ivX5g82nBH0AxodT2Oook3ymKy8O11G1lgZwntWP5fXKh8t05HB/I7lfK/yhBot\nkhzPVIwAWzZpcgLXUYz5Zyb4cuZONeeE4m0qV8kCgYEA2KZZ9Dog2MCDKk8PpsjN\nKNNkjHhpeB+DGrx1UenD2QZNr6J8x7m2cDq3CWBGjKY6/3QjdVJzbRMFBRO8d788\na0eVcqX2Oa/5KSiYDOlIyk4kO4ju/r/bqm3/XnI9qoz71y3UI5jXusin1druMVNM\n37AGdWFCjY6MV4ujPJQm5pc=\n-----END PRIVATE KEY-----\n",
  "client_email": "tfg-findegrado@appspot.gserviceaccount.com",
  "client_id": "105851033901392910570",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/tfg-findegrado%40appspot.gserviceaccount.com"
}

cred = credentials.Certificate(conf)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'tfg-findegrado.appspot.com'
})
  
bucket = storage.bucket();  

##blob.uploadFile('frame0.jpg')
i=0
while(True):
	blob = bucket.blob('cam/newCam.jpg')
	name = "data/frame" + str(i) + ".jpg"
	print("Creando " + name)
  	blob.upload_from_filename(filename=name)
	i+=1;

