import requests
import bs4

url="https://automatetheboringstuff.com/"
f=open("Content.txt","w", encoding="UTF-8")
result=requests.get(url)
soup=bs4.BeautifulSoup(result.text,"html.parser")
book_list=soup.find_all(name="li")
for i in book_list:
    # print(i.getText())
    f.write(f"{i.getText()}\n")
