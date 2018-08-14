import requests
res = requests.get("http://ya.ru")
page_source = res.text
print(page_source)