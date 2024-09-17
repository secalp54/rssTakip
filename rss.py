import xml.etree.ElementTree as ET
from docx import Document
import requests
import feedparser

input("Rss programına hoşgeldiniz.Devam etmek için enter tuşuna basınız.")
items=[]
class Item:
  def __init__(self, link, title):
    self.link = link
    self.title = title

f = open("haber.txt", "r")

for line in f:
    line=line[:-1]
    response=requests.get(line)
    root=ET.fromstring(response.content)
    for item in root.findall('.//item'):
        link = item.find('link').text
        title = item.find('title').text
        items.append(Item(link,title))

print(len(items))
bulunanLinkler=[]
keywords= open("keywords.txt", "r", encoding="utf-8")
for haber in items:
   for k in keywords:
      k=k.strip()
      k=k[:-1]
      if k.upper() in haber.title.upper().strip():
         bulunanLinkler.append(haber.link)
         break

print(bulunanLinkler)
document = Document()
for bulunan in bulunanLinkler:
   print(bulunan)
   document.add_paragraph(bulunan)
input("işlem tamamlandı. Linkler word dosyasın oluşturulacak. Devam için enter tuşuna basınız.")
document.save("linkler.docx")