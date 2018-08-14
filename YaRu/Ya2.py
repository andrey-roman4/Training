import requests

res = requests.get("https://yandex.ru/search/?text=testing")
page_source = res.text

results = page_source.split("serp-adv__found")[1].split(">")[0].split("</div")[0]
print(results)