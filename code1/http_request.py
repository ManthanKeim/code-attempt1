from urllib import request
data= request.urlopen(url="https://en.wikipedia.org/wiki/Iron_Man")
print(data.read)
print(data.version)
print(data.status)
