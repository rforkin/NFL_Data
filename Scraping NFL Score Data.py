# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:40:07 2018

@author: Richey Forkin
"""

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd 
import itertools as ite
year_url = list(range(2010,2020)) #list(range(2010,2020))
df = pd.DataFrame(columns = [])
week_url = list(range(1,18))
for yea_url, wee_url in ite.product(year_url, week_url):
#for yea_url in year_url:
#while year_url < 2020:
#    url = 'https://www.pro-football-reference.com/years/' + str(year_url) + '/week_10.htm'
    url = 'https://www.pro-football-reference.com/years/' + str(yea_url) + '/week_' + str(wee_url) + '.htm'
    r = requests.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    column_names = ('date', 'away_team', 'away_score', 'final_ot', 'home_team',  'home_score', 'total_score', 'year', 'week')
   # year_count = yea_url
 #   while year_count < 10 :
    tables=soup.find_all("table","teams",[0])
 #   print(tables)
    for row in tables:
        try:
            col=row.find_all('td')
            date = col[0].string.strip()
            away_team = col[1].a.string.strip()
            away_score = int(col[2].get_text())
            final_ot = col[3].a.string.strip()
            home_team = col[4].a.string.strip()
            home_score = int(col[5].get_text())
            year = yea_url
            week = wee_url
            final_data = [(date, away_team, away_score, final_ot, home_team, home_score, (away_score + home_score), year, week)]
            df = df.append(final_data)

        except:
            pass
 #   year_url=year_url + 1
#print(df)                       
#    year_url=year_url+1

df.to_csv("C:\\Users\\Richey Forkin\\NFL_FB_SCORES_2010_2018.csv", header = column_names)

#for kr in data2:
#   print kr.find_all("h4",{"class":"store-name"})[0].text
#   print kr.find_all("span",{"class":"desk-add jaddt"})[0].text

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 21:40:07 2018

@author: Richey Forkin
"""

from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen 

f=open("C:\\Users\\Richey Forkin\\outfileESPN.csv","w")
x=1
while(x<500):
   soup=BeautifulSoup(urlopen("http://games.espn.go.com/ffl/tools/projections?startIndex="+str(x)).read(),'html')

##   tables=soup.find("table",{'class':"playerTableTable tableBody"})
   for text in soup.find_all('tr'):
      #kr= row.findAll('tr')[2:]
      print(soup.get_text())
f.close   
      #print kr[0].text
      
      col=row.findAll('td')
      try:
         name=col[0].a.string.strip()
         pts = col[13].string.strip()
         pts.week13 = pts
         f.write(name + ',' + pts.week13 +'\n')
      except:
         pass

   x=x+40

f.close
#for kr in data2:
#   print kr.find_all("h4",{"class":"store-name"})[0].text
#   print kr.find_all("span",{"class":"desk-add jaddt"})[0].text