import requests,pandas as pd
from bs4 import BeautifulSoup
url="https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"

# Get html
r=requests.get(url)
#htmlContent=r.content
dfs=pd.read_html(r.text)
soup=BeautifulSoup(r.content,'html.parser')
#print(soup.prettify)
# html Tree Traversal


i=1
content = soup.find_all('td')

print("Countries\t|\tCases\t|\tDeaths\t|\tRegion")
for elem in content:
    if i<4:
        print(elem.text,end="\t|\t")
        i+=1
    else:
        print(elem.text)
        i=1

#for i in covid19_table.keys():
 #   print(covid19_table[i])



#print(dfs[0])
