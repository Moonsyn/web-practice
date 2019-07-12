#!C:\Users\msy94\AppData\Local\Programs\Python\Python37\python.exe
#!python3
#-*- coding: utf-8 -*-
import sys
import codecs
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove("data/"+pageId)

#Redirection
print("Location: index.py")
print()