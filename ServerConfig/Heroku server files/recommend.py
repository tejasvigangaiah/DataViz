import os
import json
from flask import Flask
from flask.ext.cors import CORS, cross_origin
from flask import request
import pymongo
import sys, traceback


app = Flask(__name__)
cors =  CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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

@app.route("/")
@cross_origin()
def helloWorld():
  return "HELLO WORLD"

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

		# Connect to Mongo
		conn = pymongo.MongoClient(MONGODB_URI)

		# Get the default database
		db = conn.get_default_database()

		# Get the data collection
		yelpmodel = db['yelpmodel']

		count = 0

		# Query the collection
		cursorPref1 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[0]).limit(10)

		recPref = list()
		rank = 1
		# Collect all the records
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

		# Query the collection
		cursorPref2 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[1]).limit(10)

		rank = 1
		# Collect all the records
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

		# Query the collection
		cursorPref3 = yelpmodel.find({"state":state, "$or" : category}).sort(preferenceList[2]).limit(10)

		rank = 1
		# Collect all the records
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
		recommendation = sorted(recPref, key=operator.itemgetter("avgscore"))
		top10 = [recommendation[x] for x in range(10)]
		# Close connection
		conn.close()
		return json.dumps(top10)
	
	except:
		traceback.print_exc(file=sys.stdout)
		return "ERROR"

@app.route("/recommendOne")
@cross_origin()
def testOne():

	try:
		# Read from query strings
		location = request.args.get('location')
		categories = request.args.get('categories')
		preference = request.args.get('preferences')

		# Split the input requirements
		categoryList = categories.split(',')
		category = [{"categories":x} for x in categoryList]

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

		count = 0

		# Query the collection
		cursorPref1 = yelpmodel.find({"state":state, "$or" : category}).sort(preference).limit(10)

		recPref = list()
		rank = 1
		# Collect all the records
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
		    recPref[count]["avgscore"] = doc[preference]
		    recPref[count]["stats"] = "Ranked " + str(rank) + " in '" + preference + "' category"
		    rank += 1
		    count += 1

		# Close connection
		conn.close()
		return json.dumps(recPref)
	
	except:
		traceback.print_exc(file=sys.stdout)
		return "ERROR"
	
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)