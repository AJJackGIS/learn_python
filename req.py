import requests

query = "哈哈"

url = f"https://www.sogou.com/web?query=${query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)

print(resp.text)
