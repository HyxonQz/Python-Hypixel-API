from tools.requests import API
import time
api = API(key = "ac8ecc62-a6e2-4ba7-ab92-1b2781bf2477")

async def main():
    start = time.time()
    guild = await api.get_guild_by_player(uuid = "9593326f76d54e0ca5d25e08787adf57")
    midpoint = time.time()
    guild = await api.get_guild_by_player(uuid = "9593326f76d54e0ca5d25e08787adf57")
    end = time.time()
    print("first request:", midpoint-start)
    print("second request:", end-midpoint)

import asyncio
asyncio.run(main())