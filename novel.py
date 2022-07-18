# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}


import requests
import json
import asyncio
import aiohttp
import aiofiles


async def download(title, cid, book_id):
    book = {"book_id": book_id, "cid": f"{book_id}|{cid}", "need_bookinfo": 1}
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={json.dumps(book)}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            content = data["data"]["novel"]["content"]
            async with aiofiles.open(f"novel/{title}.txt", mode="w", encoding="utf-8") as f:
                await f.write(content)
    print("over!" + title)


async def get_catalog(url):
    resp = requests.get(url)
    items = resp.json()["data"]["novel"]["items"]
    tasks = []
    for item in items:
        title = item["title"]
        cid = item["cid"]
        # tasks.append(download(title, cid, book_id))
        tasks.append(asyncio.create_task(download(title, cid, book_id)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + book_id + '"}'
    # asyncio.run(getCatalog(url))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_catalog(url))
