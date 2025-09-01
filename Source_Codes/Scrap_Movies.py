import requests
from bs4 import BeautifulSoup
url="https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular?page=2"
f=open("Movies_List.txt","w",encoding="UTF-8")
response=requests.get(url)
website_html=response.text
soup=BeautifulSoup(website_html,"html.parser")
all_movies=soup.find_all(name="span", class_="p--small")
# print(all_movies)

list_of_movies=[i.getText() for i in all_movies]

for i in list_of_movies:
    f.write(f"{i}\n")