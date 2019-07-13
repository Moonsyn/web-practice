#!C:\Users\msy94\AppData\Local\Programs\Python\Python37\python.exe
#!python3
#-*- coding: utf-8 -*-
import sys
import codecs
import os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi
import cgitb, view
cgitb.enable()
print("Content-Type: text/html; charset=utf-8\r\n")
print()
form = cgi.FieldStorage()
if "id" in form:
  pageId = form["id"].value
  description = open("data/"+pageId, encoding="utf-8").read()
else:
  pageId = "Welcome"
  description = "Hello Web"
print(pageId)
print("""<!DOCTYPE html>
<html lang="KR" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
    <h1><a href="index2.py?id=Angel">{desc}</a></h1>
    <a href = "create.py">create</a>
    <form action = "process_update.py" method="post">
        <input type="hidden" name = "pageId" value = "{form_default_title}">
        <p><input type="text" name = "title" placeholder = "title" value = "{form_default_title}"></p>
        <p><textarea rows="4" name = "description" placeholder = "description">{form_default_description}</textarea></p>
        <p><input type="submit"></p>
    </form>
    <ol>
      {listdir}
    </ol>
  </body>
</html>
""".format(title="Airsoft Hobby", desc = description, listdir = view.getList(), form_default_title = pageId, form_default_description = description))