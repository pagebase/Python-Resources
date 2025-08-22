import requests,bs4

byte_codes=[]
img_url=[]
website_url=""
result=requests.get(url)
soup=bs4.BeautifulSoup(result.text,"lxml")
list_of_img_tag=soup.select("img")
