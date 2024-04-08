from pymongo import MongoClient

client = MongoClient(
    host="127.0.0.1",
    port = 27017
)

sample = client["sample"]

#rand = sample.create_collection(name = 'rand')
rand = sample['rand']

print(sample.list_collection_names())

data = [
  {"name": "Melthouse","bread":"Wheat","sauce": "Ceasar"},
  {"name": "Italian BMT", "extras": ["pickles","onions","lettuce"],"sauce":["Chipotle", "Aioli"]},
  {"name": "Steakhouse Melt","bread":"Parmesan Oregano"}, 
  {"name": "Germinal", "author":"Emile Zola"}, 
  {"pastry":"cream puff","flavour":"chocolate","size":"big"}
]

rand.insert_many(data)
