from typing import Dict, Tuple
import requests

api_url = "http://localhost:8080"

class TailDatabase:
    def tails(self):
        resp = requests.get(url=api_url + "/tail")
        data = resp.json()

        return data
    
    def tail_reveal(self, coin_id: str):
        resp = requests.get(url=api_url + f"/tail/reveal/{coin_id}")
        data = resp.json()

        return data["tail_reveal"]
    
    def nft_uri(self, launcher_id: str):
        resp = requests.get(url=api_url + f"/nft/{launcher_id}")
        data = resp.json()

        return data["uri"]
