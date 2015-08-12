from pymongo import MongoClient
client = MongoClient()
db = client["prom-mongo"]

def extract_data(data):
  for row in data.split(','):
      yield from row.split(';')

new_entry = {k: v for k, v in extract_data(sys.argv[1])}

db.entries.insert_one(new_entry)