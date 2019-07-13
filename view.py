import os
from html_sanitizer import Sanitizer
def getList():
  sanitizer = Sanitizer()
  number_list = ""
  for file in os.listdir("C:/Bitnami/wampstack-7.3.6-2/apache2/htdocs/data"):
    number_list = number_list + "<li><a href = 'index.py?id={name}'>{name}</a></li>".format(name = file)
  number_list = sanitizer.sanitize(number_list)
  return number_list