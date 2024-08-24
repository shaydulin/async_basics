import asyncio
from itertools import count


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


async def print_nums():
    for num in count(0):
        print(num)
        await asyncio.sleep(1)


async def print_time():
    for cnt in count(0, 3):
        print(f"{cnt} seconds passed.")
        await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
