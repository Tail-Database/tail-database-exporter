from typing import Dict
from tail import Tail
from tail_database import TailDatabase

search_index: Dict[str, Tail] = {}

tail_database = TailDatabase()

for tail in tail_database.tails():
    tail_reveal = tail_database.tail_reveal(tail["eveCoinId"])
    nft_uri = tail_database.nft_uri(tail["launcherId"])

    tail = Tail(
        tail["hash"],
        tail["name"],
        tail["code"],
        tail["description"],
        tail["category"],
        tail["launcherId"],
        tail["eveCoinId"],
        tail_reveal,
        nft_uri
    )

    search_index[tail.hash] = tail
    search_index[tail.code] = tail
    search_index[tail.name] = tail
