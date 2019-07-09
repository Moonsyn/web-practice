#!C:\Users\msy94\AppData\Local\Programs\Python\Python37\python.exe
#!python3
#-*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html; charset=utf-8\r\n")
print()
cgi.test()