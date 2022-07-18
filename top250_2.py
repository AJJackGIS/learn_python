import requests
import bs4
import csv
import re

f = open("data_2.csv", mode="w", encoding="utf-8", newline="")

writer = csv.writer(f)

url = "https://movie.douban.com/top250"

start = 0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

reg = r"\d+"

for i in range(0, 10):
    start = i * 25
    params = {
        "start": start
    }

    resp = requests.get(url, headers=headers, params=params)

    content = resp.text

    result = bs4.BeautifulSoup(content, "html.parser")

    ol = result.find("ol", attrs={"class": "grid_view"})

    lis = ol.find_all("li")

    for li in lis:
        img = li.find("img")
        src = img.attrs["src"]

        title_span = li.find("span", attrs={"class": "title"})
        title = title_span.text

        year_p = li.find("p", attrs={"class": ""})
        year = re.search(reg, year_p.text, re.S).group()

        spans = li.find("div", attrs={"class": "star"}).find_all("span")

        score_span = spans[1]
        score = score_span.text

        total_span = spans[3]
        total = re.search(reg, total_span.text, re.S).group()

        brief_span = li.find("span", attrs={"class": "inq"})
        brief = "" if brief_span is None else brief_span.text

        writer.writerow([src, title, year, score, total, brief])

f.close()

print("over!")
