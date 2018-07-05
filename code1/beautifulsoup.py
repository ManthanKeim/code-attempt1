from bs4 import BeautifulSoup
file = open("hello.html")
from urllib import request

def hook( f = 0 , s=0 , t=0 , forth =0 ):
    print(f,s,t,forth)


request.urlretrieve("http://techslides.com/demos/sample-videos/small.mp4", "vid.mp4", hook)
fos = open("google.html")
soup = BeautifulSoup(file.read(), "html.parser")


print(soup.a)




# s=soup.title
# print(s)
# l=soup.findAll("a")
#
# for item in l:
#     if item.has_attr("href"):
#         print(item["href"])
