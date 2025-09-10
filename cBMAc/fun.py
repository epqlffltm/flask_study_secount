import asyncio

async def q():
    print("하나도 안 맞잖아")
    await asyncio.sleep(3)
    print("q exit")

async def a():
    print("하지만 빨랐죠")
    await asyncio.sleep(1)
    print("a exit")

async def c():
    print("어떻게 되먹은 거야?")
    await asyncio.sleep(5)
    print("c exit")

async def main():
    await asyncio.gather(q(), a(), c())

asyncio.run(main())