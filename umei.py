import requests
import bs4
import os_test

url = "https://www.umei.cc/bizhitupian/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"

content = resp.text

result = bs4.BeautifulSoup(content, "html.parser")

uls = result.find_all("ul", attrs={"class": "pic-list after"})

for ul in uls:

    lis = ul.find_all("li")

    for li in lis:
        img = li.find("img")
        src = img.get("data-src")
        src = src.replace("small", "")

        # 3d0990dabe0b39f957cc5be285ee6db4.jpg
        i = src.rfind("/") + 1
        name = src[i:]

        r = requests.get(src)
        r.encoding = "utf-8"

        with open("img/" + name, mode="wb") as f:
            f.write(r.content)
            f.close()
            print("over!" + name)

print("over!")
