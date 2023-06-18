from aiohttp import ClientSession


async def async_get(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception(await response.json())
            else:
                return await response.json()

