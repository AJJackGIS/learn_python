import requests

url = "https://www.pearvideo.com/video_1766646"
contId = url.split("_")[1]
srcUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.9430095499203615"
headers = {
    "Referer": url,
}

resp = requests.get(srcUrl, headers=headers)

result = resp.json()

time = result["systemTime"]
srcUrl = result["videoInfo"]["videos"]["srcUrl"]

srcUrl = srcUrl.replace(time, "cont-" + contId)

file_name = srcUrl.split("/")[-1]

with open("vedio/" + file_name, mode="wb") as f:
    f.write(requests.get(srcUrl).content)
