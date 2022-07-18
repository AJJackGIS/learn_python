import requests
import re
import csv

f = open("data.csv", mode="w", encoding="utf-8", newline="")

writer = csv.writer(f)

url = "https://movie.douban.com/top250"

start = 0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

obj = re.compile(r'<li>.*?src="(?P<src>.*?)".*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<total>.*?)人评价</span>.*?<span class="inq">(?P<brief>.*?)</span>', re.S)

for i in range(0, 10):
    start = i * 25
    params = {
        "start": start
    }

    resp = requests.get(url, headers=headers, params=params)

    content = resp.text

    result = obj.finditer(content)

    for it in result:
        # print(it.group("src"))
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        # print(it.group("total"))
        # print(it.group("brief"))

        data = it.groupdict()
        data["year"] = data["year"].strip()
        writer.writerow(data.values())

f.close()

print("over!")
