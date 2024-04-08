from pymongo import MongoClient
from pprint import pprint
import re

client = MongoClient(
	host = '127.0.0.1',
	port =  27017
)

#print(client.list_database_names())
#print(client['sample'].list_collection_names)

db = client['sample']
c_zips = db['zips']

#x = c_zips.find_one()
#print(x)


#for i in list(c_zips.find({}, {"_id":0,"city":1}).limit(12)):
#	print(i)


#print(c_zips.find().distinct('state'))
#pprint(client['sample']['cie'].find_one())


#print(client["sample"]["cie"].find_one())
#exp = re.compile('^[0-9]*$')
#pprint(list(c_zips.find({'city': exp}, {'city': 1})))


pprint(
  list(
    client['sample']['cie'].aggregate(
      [
        {'$match': {'acquisitions.company.name': 'Tumblr'}},
        {'$project': {'_id': 1, 'society': '$name'}}
      ]
    )
  )
)
