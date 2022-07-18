import requests
from lxml import etree

url = "https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

content = resp.text

tree = etree.HTML(content)

goods = tree.xpath('//*[@id="J_goodsList"]/ul/li')

for good in goods:
    price = good.xpath("./div/div[2]/strong/i/text()")[0]
    title = "电脑".join(good.xpath("./div/div[3]/a/em/text()"))
    print(title, price)
