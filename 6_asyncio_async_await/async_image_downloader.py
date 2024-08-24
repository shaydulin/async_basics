import requests
import asyncio
import aiohttp
import time


URL = "https://loremflickr.com/320/240"
N = 20

##################################################
################ _Synchronous way ################
##################################################


def sync_download():
    for _ in range(N):
        write_image(get_image(URL), "sync")


def get_image(url):
    r: requests.models.Response = requests.get(url)
    return r.content


##################################################
################ Asynchronous way ################
##################################################


async def async_download():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(N):
            task = asyncio.create_task(fetch_content(URL, session))
            tasks.append(task)
        
        await asyncio.gather(*tasks)


async def fetch_content(url, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        data = await response.read()
        write_image(data, "async")


##################################################
############## Synchronous function ##############
############## for writing image #################
##################################################


def write_image(data, name):
    filename = f"{name}-{int(time.time() * 100_000)}.jpg"
    with open(f"images/{filename}", "wb") as file:
        file.write(data)


if __name__ == "__main__":
    sync_start = time.time()
    sync_download()
    sync_end = time.time()

    async_start = time.time()
    asyncio.run(async_download())
    async_end = time.time()

    print(
        f"Synchronous download of {N} \
images took: {sync_end - sync_start} seconds."
    )
    print(
        f"Asynchronous download of {N} \
images took: {async_end - async_start} seconds."
    )
