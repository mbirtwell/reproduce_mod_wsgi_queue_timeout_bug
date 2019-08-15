import asyncio
import logging
from time import time

from aiohttp import ClientSession

FORMAT = '%(asctime)-15s %(message)s'


async def doRequest(client: ClientSession, name: str, delay: int):
    logging.info(f"Starting request {name}")
    start = time()
    async with await client.get(f"http://10.0.75.1:8000/delay/{delay}/{name}") as response:
        await response.text()
        end = time()
        logging.info(f"Done request {name} status: {response.status} in: {end - start}")


async def main():
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    async with ClientSession() as client:
        long = asyncio.create_task(doRequest(client, "long", 20))
        await asyncio.sleep(0.5)
        short = asyncio.create_task(doRequest(client, "short", 2))
        await asyncio.gather(long, short)


if __name__ == '__main__':
    asyncio.run(main())
