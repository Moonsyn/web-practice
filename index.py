#!C:\Users\msy94\AppData\Local\Programs\Python\Python37\python.exe
#!python3
#-*- coding: utf-8 -*-
import sys, codecs, os
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi, cgitb
import view
cgitb.enable()
print("Content-Type: text/html; charset=utf-8\r\n")
print()
form = cgi.FieldStorage()
from html_sanitizer import Sanitizer
sanitizer = Sanitizer()
if "id" in form:
  title = pageId = form["id"].value
  description = open("data/"+pageId, encoding="utf-8").read()
  description = sanitizer.sanitize(description)
  title = sanitizer.sanitize(title)
  update_link = "<a href = 'update.py?id={pageId}'>update</a>".format(pageId = pageId)
  delete_action = '''
  <form action="process_delete.py" method="post">
    <input type = "hidden" name = "pageId" value="{}">
    <input type = "submit" value = "delete">
  </form>
  '''.format(pageId)
else:
  title = pageId = "Welcome"
  description = "Hello Web"
  update_link = ""
  delete_action = ""
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
    {update_link}
    {delete_action}
    <h2><strong>1.WE 베레타(M9시리즈)</strong></h2>
    <h3><a href="https://www.kyairsoft.com/we-m002-m925-m92-chrome.html" target="_blank">WE-M002-M925 M92 (CHROME)</a></h3><br>
    <img src="img_39318_3.jpg", width = 40%><br>
    가격 113.52 달러 -> 현재 세일해서 102달러<br>
    국내 건샵 <a href="http://www.h-guns.com/product/detail.html?product_no=4259&cate_no=367&display_group=1" target="_blank">h-guns</a>에서 21만원에 팔고 있는 것으로 확인<br>
    배송비와 총포협 검사비, 그리고 배송 기간을 따져보았을때 국내에서 사는 것도 나쁘지 않다.
    <h2><strong>2.WE 베레타(M9시리즈) honeycomb edition</strong></h2>
    <h3><a href="https://www.kyairsoft.com/we-m92-honeycomb-pistol-sliver.html" target="_blank">WE-M002-M925 M92 (CHROME)</a></h3><br>
    <img src="img_47817_3.jpg", width = 40%><br>
    가격 108.77달러<br>
    외관 자체는 상당히 간지가 나나 검색을 해도 잘 안나온다. 혹시나 하자가 있지 않을까 불안함.
    <h2><strong>3.WE 데저트 이글 SV</strong></h2>
    <h3><a href="https://www.kyairsoft.com/we-cybergun-licensed-desert-eagle-50-cal-gbb-pistol-with-marking-electroplating-silver.html" target="_blank">WE - CYBERGUN LICENSED DESERT EAGLE .50 CAL GBB PISTOL WITH MARKING (ELECTROPLATING SILVER)</a></h3><br>
    <img src="img_42225_1898_2.jpg", width = 40%><br>
    가격 164.82 달러<br>
    각인과 정식 라이센스를 받아서 가격이 상당히 나가는 편이다. 그래도 간지는 ㅇㅈ
    <h2><strong>4.KWC 미니 우지</strong></h2>
    <h3><a href="https://www.kyairsoft.com/we-cybergun-licensed-desert-eagle-50-cal-gbb-pistol-with-marking-electroplating-silver.html" target="_blank">WE - CYBERGUN LICENSED DESERT EAGLE .50 CAL GBB PISTOL WITH MARKING (ELECTROPLATING SILVER)</a></h3><br>
    <img src="KWC_SMG_UZIV2_01_default_logo_tr.png", width = 40%><br>
    가격 155 달러<br>
    CO2탄을 사용한다. 한 손으로 드르륵 갈길 수 있는게 매력.<br>
    KWC사가 2017년 전에 만든 가스총은 MP7말고 다 ㅄ이었다는게 불안 요소
    <ol>
      {listdir}
    </ol>
  </body>
</html>
""".format(title = title, desc = description, 
listdir = view.getList(), update_link = update_link, delete_action = delete_action))