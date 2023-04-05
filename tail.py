class Tail:
    hash: str
    name: str
    code: str
    description: str
    category: str
    launcher_id: str
    eve_coin_id: str
    tail_reveal: str
    nft_uri: str
    website_url: str
    twitter_url: str
    discord_url: str

    def __init__(
        self,
        hash: str,
        name: str,
        code: str,
        description: str,
        category: str,
        launcher_id: str,
        eve_coin_id: str,
        tail_reveal: str,
        nft_uri: str,
        website_url: str,
        twitter_url: str,
        discord_url: str,
    ):
        self.hash = hash
        self.name = name
        self.code = code
        self.description = description
        self.category = category
        self.launcher_id = launcher_id
        self.eve_coin_id = eve_coin_id
        self.tail_reveal = tail_reveal
        self.nft_uri = nft_uri
        self.website_url = website_url
        self.twitter_url = twitter_url
        self.discord_url = discord_url

class TailDetails:
    name: str
    code: str
    nft_uri: str

    def __init__(
        self,
        name: str,
        code: str,
        nft_uri: str,
    ):
        self.name = name
        self.code = code
        self.nft_uri = nft_uri
