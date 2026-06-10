import requests
from bs4 import BeautifulSoup

q=input("Enter your search query: ")
url="https://duckduckgo.com/html/?q="+q

r=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
soup=BeautifulSoup(r.text,"html.parser")

for i,x in enumerate(soup.find_all("a",class_="result__a")[:10],1):
    print(i,x.get_text())