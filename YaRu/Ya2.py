import requests

res = requests.get("https://yandex.ru/search/?text=testing")
page_source = res.text

results = page_source.split('class="link')[1].split('href="')[1].split('"')[0]
print(results)