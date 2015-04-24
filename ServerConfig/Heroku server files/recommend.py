import os
import json
from flask import Flask
from flask.ext.cors import CORS, cross_origin
from flask import request
import pymongo
import sys, traceback


app = Flask(__name__)
# Enable cross domain requests
cors =  CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Get the state code for corresponding cities
def getState(location):
	if location == 'Phoenix':
		return 'AZ'
	elif location == 'LasVegas':
		return 'NV'
	elif location == 'Madison':
		return 'WI'
	elif location == 'UrbanaChampaign':
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

# Default path
@app.route("/")
@cross_origin()
def helloWorld():
  return "HELLO WORLD"

# Recommendation path
@app.route("/recommend")
@cross_origin()
def test():

	try:
		# Read from query strings
		location = request.args.get('location')
		categories = request.args.get('categories')
		preference = request.args.get('preferences')

		# Split the input requirements
		categoryList = categories.split(',')
		category = [{"categories":x} for x in categoryList]
		preferenceList = preference.split(',')

		# Get the state for the given location
		state = getState(location)

		# MongoLab URL - This username and password only has read access
		MONGODB_URI = 'mongodb://dvyelp:dvyelp@ds035448.mongolab.com:35448/dv_yelp' 

		# Connect to Mongo DB
		conn = pymongo.MongoClient(MONGODB_URI)

		# Get the default database
		db = conn.get_default_database()

		# Get the data collection
		yelpmodel = db['yelpmodel']

		# Counting the index for entries
		count = 0

		# Query the collection with preference 1
		cursorPref1 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[0]).limit(10)

		# List that stores all the selected restaurants
		recPref = list()

		# Rank for the selected preference
		rank = 1

		# Collect all the records for selected preference and assign their values to the list
		for doc in cursorPref1:
		    recPref.append(dict())
		    recPref[count]["address"] = doc["address"]
		    recPref[count]["pos"] = doc["pos"]
		    recPref[count]["neg"] = doc["neg"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["star1"] = doc["star1"]
		    recPref[count]["star2"] = doc["star2"]
		    recPref[count]["star3"] = doc["star3"]
		    recPref[count]["star4"] = doc["star4"]
		    recPref[count]["star5"] = doc["star5"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["name"] = doc["name"]
		    recPref[count]["rank"] = rank
		    recPref[count]["categories"] = doc["categories"]
		    recPref[count]["avgscore"] = sum([doc[x] for x in preferenceList])
		    recPref[count]["stats"] = "Ranked " + str(rank) + " in '" + preferenceList[0] + "' category"
		    rank += 1
		    count += 1

		# Query the collection with preference 2
		cursorPref2 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[1]).limit(10)

		# Rank for the selected preference
		rank = 1

		# Collect all the records for selected preference and assign their values to the list
		for doc in cursorPref2:
		    recPref.append(dict())
		    recPref[count]["address"] = doc["address"]
		    recPref[count]["pos"] = doc["pos"]
		    recPref[count]["neg"] = doc["neg"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["star1"] = doc["star1"]
		    recPref[count]["star2"] = doc["star2"]
		    recPref[count]["star3"] = doc["star3"]
		    recPref[count]["star4"] = doc["star4"]
		    recPref[count]["star5"] = doc["star5"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["name"] = doc["name"]
		    recPref[count]["rank"] = rank
		    recPref[count]["categories"] = doc["categories"]
		    recPref[count]["avgscore"] = sum([doc[x] for x in preferenceList])
		    recPref[count]["stats"] = "Ranked " + str(rank) + " in '" + preferenceList[1] + "' category"
		    rank += 1
		    count += 1

		# Query the collection with preference 3
		cursorPref3 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[2]).limit(10)

		# Rank for the selected preference
		rank = 1

		# Collect all the records for selected preference and assign their values to the list
		for doc in cursorPref3:
		    recPref.append(dict())
		    recPref[count]["address"] = doc["address"]
		    recPref[count]["pos"] = doc["pos"]
		    recPref[count]["neg"] = doc["neg"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["star1"] = doc["star1"]
		    recPref[count]["star2"] = doc["star2"]
		    recPref[count]["star3"] = doc["star3"]
		    recPref[count]["star4"] = doc["star4"]
		    recPref[count]["star5"] = doc["star5"]
		    recPref[count]["stars"] = doc["stars"]
		    recPref[count]["name"] = doc["name"]
		    recPref[count]["rank"] = rank
		    recPref[count]["categories"] = doc["categories"]
		    recPref[count]["avgscore"] = sum([doc[x] for x in preferenceList])
		    recPref[count]["stats"] = "Ranked " + str(rank) + " in '" + preferenceList[2] + "' category"
		    rank += 1
		    count += 1

		import operator

		# Sort the selected restaurants based on its average score
		recommendation = sorted(recPref, key=operator.itemgetter("avgscore"))

		# List that stores addresses of the restaurants that have been parsed (this list is used for checking if a restaurant has already been selected into top 10)
		addresslist = list()

		# List that stores the top 10 restaurants that will be returned as json array
		top10 = list()

		# Index of the element that is being processed
		index = 0

		# This loop checks in the sorted list of restaurants if there are any repetitions and if yes, merges them into a single entry in top 10 list
		for x in range(count):
			if(recommendation[x]["address"] in addresslist):
				# Merging in case of repetition
				top10[index-1]["stats"] += ", " + recommendation[x]["stats"]
			else:
				# Append to top 10 if it is a new restaurant
				top10.append(dict())
				addresslist.append(recommendation[x]["address"])
				top10[index] = recommendation[x]
				index += 1
			if(index == 10):
				# Break loop when top 10 has been determined
				break

		# Close connection
		conn.close()
		return json.dumps(top10)
	
	except:
		traceback.print_exc(file=sys.stdout)
		return "ERROR"
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)