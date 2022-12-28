import sqlite3
from datetime import datetime
import os

def url(inn):
      outt=""
      outt=inn[8:inn[8:].find("/")+8]
      return outt

places = {}
con = sqlite3.connect(r"C:\Users\\"+os.getlogin()+"\AppData\Roaming\Mozilla\Firefox\Profiles\i6op3f7b.default\places.sqlite")
cur = con.cursor()
for row in cur.execute("SELECT * FROM moz_places;"):
      yil = row[8]
      if yil==None:
            continue
      yil = int(str(yil)[:10])
      year = datetime.utcfromtimestamp(yil).strftime('%Y')
      if(year==str(datetime.today().year)):
            site = url(row[1])
            if site not in places:
                  places[site] = 1
            else:
                  places[site]+=1
con.close()


#https://realpython.com/sort-python-dictionary/
out = dict(sorted(places.items(), key=lambda item: item[1]))

#https://stackoverflow.com/questions/22520739/python-sort-a-dict-by-values-producing-a-list-how-to-sort-this-from-largest-to
results = sorted(out.items(), key=lambda x: x[1]) 
results.reverse()

#for r in results:
#      print(r)


import random
import numpy as np
import cv2 as cv
img = np.zeros((512,512,3), np.uint8)
#cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
font = cv.FONT_HERSHEY_COMPLEX_SMALL
cv.putText(img,'we\'ve seen some great places...',(10,24), font, 1,(255,255,255),1,cv.LINE_AA)
for r  in range(0,25):
      site = results[r][0]+" ~ "+str(results[r][1])+" visits"
      cv.putText(img,site,(10,24*r + 48), font, 1,(200+random.randint(0,50),200+random.randint(0,50),200+random.randint(0,50)),1,cv.LINE_AA)
cv.imshow("pic",img)
cv.imwrite("2022.png", img)
