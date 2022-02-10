import requests
from bs4 import BeautifulSoup
import csv
# Why use try-except, Because some url don't have information
# pvid is province id, the lastest number in url
def temperature(pvid):
    try:
        r = requests.get('https://www.tmd.go.th/province.php?id='+ str(pvid))
        s = BeautifulSoup(r.text,'html.parser')

        p = s.find_all('span',{'class':'title'})
        t = s.find_all('td',{'class':'strokeme'})
        dt = s.find_all('td',{'class':'PRH'})

        province = p[0].text
        temp = t[0].text
        dtt =  dt[0].text
        
        return (province, temp, dtt)
    except:
        return 0

# why must loop 83 times, Because some pvid don't have information
data = []
for i in range(1,83):
    temperature(i)
    data.append(temperature(i))
# remove 0 from data
finaldata = []
for d in data:
    if d != 0:
        finaldata.append(d)

header = ["Province", "Temperature", "Date"]
with open('Temperature.csv','w',encoding='utf8',newline='') as f:
    fw = csv.writer(f)
    fw.writerow(header)
    fw.writerows(finaldata)










    


    

    

   
    
    



