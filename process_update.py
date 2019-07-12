#!C:\Users\msy94\AppData\Local\Programs\Python\Python37\python.exe
#!python3
#-*- coding: utf-8 -*-
import sys
import codecs
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import cgitb
cgitb.enable(display=0, logdir="exception")
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

opened_file = open(os.getcwd() + "\\data\\" + pageId, "w")
opened_file.write(description)
opened_file.close()
os.rename(os.getcwd() + "\\data\\" + pageId, os.getcwd() + "\\data\\" + title)

#Redirection
print("Location: index.py?id=" + title)
print()