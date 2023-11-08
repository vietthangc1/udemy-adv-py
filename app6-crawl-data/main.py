import requests

url = "https://tiki.vn/dien-gia-dung/c1882"

r = requests.get(url)
data = r.content
print(data)