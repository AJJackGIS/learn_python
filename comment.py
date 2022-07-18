import requests
import math
import csv

id = "108653"
music = "东方之珠"
page = 0
size = 0
brief_url = f"https://music.163.com/api/v1/resource/comments/R_SO_4_{id}?limit=0&offset=0"

f = open("comment.csv", mode="w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)

#  拿到总数
resp = requests.get(brief_url)
data = resp.json()
total = data["total"]
hotComments = data["hotComments"]

# 热门评论
for comment in hotComments:
    # msg = f'赞:{comment["likedCount"]} 昵称:{comment["user"]["nickname"]} 评论:{comment["content"]}'
    csv_writer.writerow([comment["likedCount"], comment["user"]["nickname"], comment["content"]])

# 所有的评论
size = 100
page = math.ceil(total / size)
for i in range(0, page):
    url = f"https://music.163.com/api/v1/resource/comments/R_SO_4_{id}?limit={size}&offset={i + 1}"
    comments = requests.get(url).json()["comments"]
    for comment in comments:
        # msg = f'赞:{comment["likedCount"]} 昵称:{comment["user"]["nickname"]} 评论:{comment["content"]}'
        csv_writer.writerow([comment["likedCount"], comment["user"]["nickname"], comment["content"]])

f.close()
print("over...")
