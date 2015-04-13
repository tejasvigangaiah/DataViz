import os
import json
from flask import Flask
from flask import request
import pymongo

app = Flask(__name__)

def getState(location):
	if location == 'Phoenix':
		return 'AZ'
	elif location == 'Las Vegas':
		return 'NV'
	elif location == 'Madison':
		return 'WI'
	elif location == 'Urbana-Champaign':
		return 'IL'
	elif location == 'Charolette':
		return 'NC'
	elif location == 'Pittsburgh':
		return 'PA'
	elif location == 'Waterloo':
		return 'ON'
	elif location == 'Montreal':
		return 'QC'
	elif location == 'Edinburgh':
		return 'EDH'
	elif location == 'Karlsruhe':
		return 'BW'
	else:
		return ''

@app.route("/", methods=['GET'])
def hello():
    return request.query_string

@app.route("/recommend")
def test():

	try:
		# Read from query strings
		location = request.args.get('location')
		categories = request.args.get('categories')
		preferences = request.args.get('preferences')

		# Split the input requirements
		categoryList = categories.split(',')
		category = [{"categories":x} for x in categoryList]
		preferenceList = preferences.split(',')
		preference = [(x, pymongo.DESCENDING) for x in preferenceList]

		# Get the state for the given location
		state = getState(location)

		# MongoLab URL - This username and password only has read access
		MONGODB_URI = 'mongodb://dvyelp:dvyelp@ds035448.mongolab.com:35448/dv_yelp' 

		# Connect to Mongo
		conn = pymongo.MongoClient(MONGODB_URI)

		# Get the default database
		db = conn.get_default_database()

		# Get the data collection
		yelpmodel = db['yelpmodel']

		# Query the collection
		cursor = yelpmodel.find({"state":state, "$or" : category}).sort(preference).limit(10)

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
		    recommendation[rank-1]["name"] = doc["name"]
		    recommendation[rank-1]["rank"] = rank
		    recommendation[rank-1]["categories"] = doc["categories"]
		    rank += 1
		# Close connection
		conn.close()
		return json.dumps(recommendation)
	except:
		return "Insuffecient Inputs"
	#categories = category.split(',')
	#return json.dumps({"location": location, "category": category})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)