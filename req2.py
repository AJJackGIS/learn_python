import requests

query = "dog"

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": query
}

resp = requests.post(url, data=data)

result = resp.json()["data"]

for item in result:
    print(item["k"] + ' --- ' + item["v"])

print(result)
