import jsonpickle
from typing import Dict
from config import Config
from tail import Tail
from tail_database import TailDatabase

if Config.output_directory is None:
    raise Exception("TAILDB_EXPORTER_OUTPUT_DIR must be set")

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

    tail_json = jsonpickle.encode(tail, unpicklable=False)

    with open(Config.output_directory + f"/{tail.hash}.json", 'w+') as f:
        f.write(tail_json)

search_index_json = jsonpickle.encode(search_index, unpicklable=False)

with open(Config.output_directory + f"/search_index.json", 'w+') as f:
    f.write(search_index_json)
