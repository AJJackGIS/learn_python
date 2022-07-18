import requests
from lxml import etree

domain = "https://m.dytt8.net"
url = domain + "/html/gndy/dyzz/index.html"
resp = requests.get(url)
resp.encoding = "gb2312"
content = resp.text
tree = etree.HTML(content)
tables = tree.xpath('//table[@class="tbspan"]')

for table in tables:
    title = table.xpath("./tr[2]/td[2]/b/a/text()")[0]
    src = table.xpath("./tr[2]/td[2]/b/a/@href")[0]
    time = table.xpath("./tr[3]/td[2]/font/text()")[0].lstrip("日期：").rstrip()

    print(title, time)
    page = domain + src
    resp = requests.get(page)
    resp.encoding = "gb2312"
    content = resp.text
    tree = etree.HTML(content)
    download = tree.xpath('//*[@id="Zoom"]/td/a/@href')
    print(download)
