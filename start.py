import jsonpickle
from typing import Dict, List
from config import Config
from tail import Tail
from tail_database import TailDatabase

if Config.output_directory is None:
    raise Exception("TAILDB_EXPORTER_OUTPUT_DIR must be set")

search_index: Dict[str, str] = {}
tails: List[Tail] = []

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

    tails.append(tail)
    search_index[tail.hash] = tail.hash
    search_index[tail.code] = tail.hash
    search_index[tail.name] = tail.hash

    tail_json = jsonpickle.encode(tail, unpicklable=False)

    with open(Config.output_directory + f"/{tail.hash}.json", 'w+') as f:
        f.write(tail_json)

search_index_json = jsonpickle.encode(search_index, unpicklable=False)
tails_json = jsonpickle.encode(tails, unpicklable=False)

with open(Config.output_directory + f"/search_index.json", 'w+') as f:
    f.write(search_index_json)

with open(Config.output_directory + f"/tails.json", 'w+') as f:
    f.write(tails_json)
