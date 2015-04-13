import pymongo

# MongoLab URL - This username and password only has read access
MONGODB_URI = 'mongodb://dvyelp:dvyelp@ds035448.mongolab.com:35448/dv_yelp' 

# Connect to Mongo
conn = pymongo.MongoClient(MONGODB_URI)

# Get the default database
db = conn.get_default_database()

# Get the data collection
yelpmodel = db['yelpmodel']

categories = 'Indian,Italian'
categoryList = categories.split(',')
category = [{"categories":x} for x in categoryList]
preferences = 'recommend,quick'
preferenceList = preferences.split(',')
preference = [(x, pymongo.DESCENDING) for x in preferenceList]
# Query the collection
cursor = yelpmodel.find({"city":"Phoenix", "$or" : category}).sort(preference).limit(1)

recommendation = list()

rank = 1
# Collect all the records
for doc in cursor:
    recommendation.append(dict())
    recommendation[rank-1]["address"] = doc["address"]
    recommendation[rank-1]["pos"] = doc["pos"]
    recommendation[rank-1]["neg"] = doc["neg"]
    recommendation[rank-1]["stars"] = doc["stars"]
    recommendation[rank-1]["star1"] = doc["star1"]
    recommendation[rank-1]["star2"] = doc["star2"]
    recommendation[rank-1]["star3"] = doc["star3"]
    recommendation[rank-1]["star4"] = doc["star4"]
    recommendation[rank-1]["star5"] = doc["star5"]
    recommendation[rank-1]["stars"] = doc["stars"]
    recommendation[rank-1]["rank"] = rank
    recommendation[rank-1]["categories"] = doc["categories"]
    rank += 1


print(recommendation)
# Close connection
conn.close()