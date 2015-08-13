import sys

from pymongo import MongoClient

client = MongoClient()
db = client["prom-mongo"]


def extract_data(data):
    for row in data.split(','):
        yield row.split(';')


new_entry = {k: v for k, v in extract_data(sys.argv[1])}

result = db.entries.insert_one(new_entry)
print(result.inserted_id)
