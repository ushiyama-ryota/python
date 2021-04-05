import re#文字列の検索
import requests#webページの読み込み
from pathlib import Path as path#ファイルの操作
from bs4 import BeautifulSoup as bs#htmlの検索
import cv2#画像処理
import time#処理にインターバルを設ける
import urllib.request as req#urlから画像をダウンロード
import os#フォルダー指定のため
from PIL import Image as im#画像リサイズのため
import matplotlib.pyplot as plt
from io import BytesIO#画面リサイズで画像よ呼び込むため


#出力するファイルを作成
output_folder=path("画像")
#print(help(path.mkdir))
output_folder.mkdir(mode=511, parents=False, exist_ok=True)

#対象のurl
url="https://www.photo-ac.com/main/search?q=%E7%8C%AB&qt=&qid=&creator=&ngcreator=&nq=&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&sl=ja&pp=70&p=2"

#対象のページ(html)から、必要な部分を取り出す
html=requests.get(url).text
soup=bs(html,"html.parser")#lxml=python内のhtml
#print(soup.prettify())
#print(help(bs.find_all))
#pre_list=soup.find_all("div",attrs={"class":"photo-img item"}).find_all("img",attrs={"class":"thumbnail lazy"})
pre_list=soup.find_all("img",attrs={"class":"thumbnail lazy"})
#for i in pre_list:print(i)

#urlを格納する
linklist=[]
for list in pre_list:
    link_url=list.attrs["data-src"]
    linklist.append(link_url)
#for i in linklist:print(i)
"""
#画像の名前を格納する
linkname=[]
for list in pre_list:
    title=list.attrs["title"]
    linkname.append(title)
#for i in linkname:print(i)
#print(len(linklist),len(linkname))
#print(type(linkname))
#print(help(req.urlretrieve))
"""

for i in range(0,len(linklist)-1):
    #img=req.urlretrieve(linklist[i])
    img=req.urlretrieve(linklist[i],os.path.join(output_folder,"画像"+str(i)+".png"))
    #img=cv2.imread(linklist[i])
    #print(linkname[i])
    #time.sleep(1.0)

#print(help(im.open))

#出力するファイルを作成
resize_output_folder=path("resiz_画像")
resize_output_folder.mkdir(mode=511, parents=False, exist_ok=True)
for i in range(0,len(linklist)-1):
    print(i)
    if os.path.exists(os.path.join(output_folder,"画像"+str(i)+".png")):
        img=im.open(os.path.join(output_folder,"画像"+str(i)+".png"))
        #if img==None:print(linkname[i])
        small_img=img.resize((128,128))
        #plt.imshow(small_img)
        small_img.save(os.path.join(resize_output_folder,"resize_画像"+str(i+68)+".png"))
    else: print("画像"+str(i)+".png")
