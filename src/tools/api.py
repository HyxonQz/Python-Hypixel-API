from tools.asynchttp import async_get
from tools.classes import Guild, Player, SkyblockProfile
from tools.ratelimiter import Ratelimiter
from cache3 import MiniCache


class API:
    def __init__(self, key: str, maxRequests: int = 60, cacheTTL: int = 600, cacheSize: int = 1000):
        if cacheTTL > 0 and cacheSize > 0:
            self.cache = MiniCache(name = "Cache", max_size = cacheSize)
            self.cacheTTL: int = cacheTTL
        else:
            self.cache = None

        self.key: str = key
        self.maxRequests: int = maxRequests
        self.rateLimiter: Ratelimiter = Ratelimiter(maxRequests = maxRequests)


    BASE_URL = "https://api.hypixel.net"


    async def get_guild_by_id(self, id: str) -> Guild:
        response: dict = await self.__request__(path="guild", parameters={"id": id})
        return Guild(response.get("guild", None))


    async def get_guild_by_player(self, uuid: str) -> Guild:
        response: dict = await self.__request__(path="guild", parameters={"player": uuid})
        return Guild(response.get("guild", None))


    async def get_player_by_name(self, name: str) -> Player:
        response: dict = await self.__request__(path="player", parameters={"name": name})
        return Player(response.get("player", None))


    async def get_player_by_uuid(self, uuid: str) -> Player:
        response: dict = await self.__request__(path="player", parameters={"uuid": uuid})
        return Player(response.get("player", None))    


    async def get_skyblock_profile_by_id(self, profileId: str) -> SkyblockProfile:
        response: dict = await self.__request__(path="skyblock/profile", parameters={"profile": profileId})
        return SkyblockProfile(response.get("profile", None))  
    

    async def get_skyblock_profiles_by_player(self, uuid: str) -> list[SkyblockProfile]:
        response: dict = await self.__request__(path="skyblock/profiles", parameters={"uuid": uuid})
        return [SkyblockProfile(profile) for profile in response.get("profile", None)]
    

    async def __request__(self, path: str, parameters: dict = {}) -> dict:
        query = f"key={self.key}"
        for key, value in parameters.items():
            query += f"&{key}={value}"

        if self.cache is not None:
            cached = self.cache.get(query)
            if cached is not None:
                return cached

        await self.rateLimiter.execute()
        response = await async_get(url=f"{self.BASE_URL}/{path}?{query}")
        self.cache.set(key=query, value=response, timeout=self.cacheTTL)
        return response

