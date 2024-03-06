import json
from pathlib import Path
from random import sample
from quart import request

class Handler():
    def __init__(self):
        path = Path(__file__).parent / "./dataset.jsonl"
        with open(path) as f:
            self.records = [json.loads(x) for x in f]
    
    def get_random(self):
        count = request.args.get("count", type=int)
        if not count:
            count = 1
        
        selected_records = sample(self.records, count)
        return json.dumps(selected_records)
        