class Guild:
    def __init__(self, guild: dict):
        self.name: str|None = guild.get("name", None)
        self.tag: str|None = guild.get("tag", None)
        self.description: str|None = guild.get("description", None)
        self.members: list[Member]|list = [Member(member) for member in guild.get("members", [])]
        self.exp: int = guild.get("exp", 0)
        self.created: int = guild.get("created", 0)
        self.colour: str = guild.get("tagColor", "GRAY")

    def get_member(self, uuid):
        return [member for member in self.members if member.uuid == uuid][0]

class Member:
    def __init__(self, member: dict):
        self.uuid: str = member.get("uuid", None)
        self.rank: str = member.get("rank", {})
        self.joined: int = member.get("joined", None)
        self.mutedTill: int = member.get("mutedTill", None)
        self.guildExp: dict[str:int] = member.get("expHistory", {})

class Rank:
    def __init__(self, rank: dict):
        self.name: str = rank.get("name", None)
        self.default: bool = rank.get("default", False)
        self.tag: str = rank.get("tag", None)
        self.created: int = rank.get("created", 0)
        self.priority: int = rank.get("priority", 0)

class Player:
    def __init__(self, player: dict):
        self.uuid: str = player.get("uuid", None)
        self.displayName: str = player.get("displayname", None)
        self.playerName: str = player.get("playername", None)
        self.firstLogin: int = player.get("firstLogin", 0)
        self.lastLogin: int = player.get("lastLogin", 0)
        self.lastLogout: int = player.get("lastLogout", 0)
        self.networkExp: int = player.get("networkExp", 0)
        self.achievementPoints: int = player.get("achievementPoints", 0)
        self.rank: str = player.get("newPackageRank", None)
        self.plusColour: str = player.get("rankPlusColor", None)
        self.karma: int = player.get("karma", 0)
        self.socialMedia: SocialMedia = player.get("socialMedia", {})

class SocialMedia:
    def __init__(self, socialMedia: dict) -> None:
        socialMedia: dict = socialMedia.get("links", {})
        self.youtube: str = socialMedia.get("youtube", None)
        self.twitch: str = socialMedia.get("twitch", None)
        self.twitter: str = socialMedia.get("twitter", None)
        self.discord: str = socialMedia.get("discord", None)
        self.hypixel: str = socialMedia.get("hypixel", None)
        self.instagram: str = socialMedia.get("instagram", None)
        self.tiktok: str = socialMedia.get("tiktok", None)

