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
number_list = ""
for file in os.listdir("C:/Bitnami/wampstack-7.3.6-2/apache2/htdocs/data"):
  number_list = number_list + "<li><a href = 'index.py?id={name}'>{name}</a></li>".format(name = file)
print("""<!DOCTYPE html>
<html lang="KR" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
    <h1><a href="index2.py?id=Angel">{desc}</a></h1>
    <a href = "create.py">create</a>
    <form action = "process_create.py" method="post">
        <p><input type="text" name = "title" placeholder = "title"></p>
        <p><textarea rows="4" name = "description" placeholder = "description"></textarea></p>
        <p><input type="submit"></p>
    </form>
    <ol>
      {listdir}
    </ol>
  </body>
</html>
""".format(title="Airsoft Hobby", desc = description, listdir = number_list))