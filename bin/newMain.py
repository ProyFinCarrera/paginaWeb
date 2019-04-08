#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by: Jairo Gonzalez Lemus alu0100813272@ull.edu.es
# File fingers.py:
# 1. Execution of the fingerprint recognition system.
# 2. Downloading data from firebase to find similarity with other data.
# 3. Registration of date in firebase
# 4. The double identification is verified
import subprocess

datos = ['sudo','python', './bin/main.py',"otro"]
# datos = ['./fingers.py', name]
subprocess.Popen(datos,stderr=subprocess.PIPE)
