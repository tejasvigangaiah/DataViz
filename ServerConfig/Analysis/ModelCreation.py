import pymongo
from textblob import TextBlob
import nltk
import json


# Create the dictonary with initial values
def create_rating_dict():
	return {"pos":0, "neg":100, "star1":0, "star2":0, "star3":0, "star4":0, "star5":0, "accurate":0, "ambience":0, "bake":0, "best":0, 
	"commitment":0, "confidence":0, "delivery":0, "different":0, "economy":0, "enormous":0, "excellent":0, "fantastic":0, 
	"filling":0, "flavor":0, "fresh":0, "friendly":0, "grow":0, "happy":0, "honest":0, "hot":0, "love":0, "memorable":0, 
	"neighborhood":0, "new":0, "pleasant":0, "price":0, "quality":0, "quick":0, "reasonable":0, "recommend":0, "service":0, 
	"special":0, "stuff":0, "sturdy":0, "surprise":0, "taste":0, "together":0, "worth":0}


# Connection to Mongo DB
try:
	conn=pymongo.MongoClient()
except pymongo.errors.ConnectionFailure:
	print ("Could not connect to MongoDB")

# Connecting to the yelp dataset DB
db = conn.yelpdb

# Opening collections
b_coll = db.business # Business collection
r_coll = db.review # Review collection

rating = dict()
# Read the list of businesses
businesses = b_coll.find({"categories" : "Restaurants"}, timeout=False)
count = 0
# For each business read in the above line
for business in businesses:
	count += 1
	b_id = (business["business_id"])
	reviews = r_coll.find({"business_id" : b_id}, timeout=False) # Find set of reviews for the given business
	
	# These values store the number of positive and negative reviews for the place and number of reviews
	pos = 0
	neg = 0
	review_count = 0

	# Create an empty dictionary
	rating = create_rating_dict()

	# For each review for the selected business
	print(count)
	for review in reviews:
		review_count += 1
		text = review["text"] # The review text
		stars = review["stars"]	# Number of stars given by the reviewer
		blob = TextBlob(text)
		polarity = blob.sentiment.polarity # Find polarity of the text (Value between -1 and 1)

		# Calculating number of positive and negative reviews
		if polarity > 0:
			pos += 1 
		else:
			neg += 1

		# Setting values for each measure
		if "accurate" in text.lower() or "correct" in text.lower():
			rating["accurate"] += polarity
		if "ambience" in text.lower() or "luxur" in text.lower() or "rich" in text.lower() or "grand" in text.lower():
			rating["ambience"] += polarity
		if "bake"  in text.lower():
			rating["bake"] += polarity
		if "best" in text.lower():
			rating["best"] += polarity
		if "commit" in text.lower():
			rating["commitment"] += polarity
		if "confiden" in text.lower() or "trust" in text.lower() or "believe" in text.lower():
			rating["confidence"] += polarity
		if "deliver" in text.lower():
			rating["delivery"] += polarity
		if "different" in text.lower():
			rating["different"] += polarity
		if "econom" in text.lower():
			rating["economy"] += polarity
		if "big" in text.lower() or "huge" in text.lower() or "enormous" in text.lower():
			rating["enormous"] += polarity
		if "excellent" in text.lower():
			rating["excellent"] += polarity
		if "fantastic" in text.lower():
			rating["fantastic"] += polarity
		if "filling" in text.lower():
			rating["filling"] += polarity
		if "flavor" in text.lower():
			rating["flavor"] += polarity
		if "fresh" in text.lower():
			rating["fresh"] += polarity
		if "friend" in text.lower() or "courteous" in text.lower():
			rating["friendly"] += polarity
		if "grow" in text.lower():
			rating["grow"] += polarity
		if "happy" in text.lower() or "glad" in text.lower():
			rating["happy"] += polarity
		if "honest" in text.lower():
			rating["honest"] += polarity
		if "hot" in text.lower():
			rating["hot"] += polarity
		if "love" in text.lower() or "like" in text.lower():
			rating["love"] += polarity
		if "memorable" in text.lower():
			rating["memorable"] += polarity
		if "neighbor" in text.lower() or "closest" in text.lower():
			rating["neighborhood"] += polarity
		if "new" in text.lower():
			rating["new"] += polarity
		if "pleasant" in text.lower():
			rating["pleasant"] += polarity
		if "price" in text.lower() or "afford" in text.lower() or "cost" in text.lower() or "pocket-friendly" in text.lower():
			rating["price"] += polarity
		if "quality" in text.lower():
			rating["quality"] += polarity
		if "quick" in text.lower() or "fast" in text.lower():
			rating["quick"] += polarity
		if "reasona" in text.lower():
			rating["reasonable"] += polarity
		if "recommend" in text.lower():
			rating["recommend"] += polarity
		if "service" in text.lower():
			rating["service"] += polarity
		if "special" in text.lower():
			rating["special"] += polarity
		if "stuff" in text.lower() or "load" in text.lower():
			rating["stuff"] += polarity
		if "sturdy" in text.lower():
			rating["sturdy"] += polarity
		if "surprise" in text.lower() or "excite" in text.lower() or "amaze" in text.lower() or "afford" in text.lower():
			rating["surprise"] += polarity
		if "taste" in text.lower() or "delicious" in text.lower() or "mouth water" in text.lower():
			rating["taste"] += polarity
		if "together" in text.lower():
			rating["together"] += polarity
		if "worth" in text.lower() or "great" in text.lower():
			rating["worth"] += polarity

		# Calculating number of 1 stars, 2 stars etc.
		if stars == 1:
			rating["star1"] += 1
		elif stars == 2:
			rating["star2"] += 1
		elif stars == 3:
			rating["star3"] += 1
		elif stars == 4:
			rating["star4"] += 1
		elif stars == 5:
			rating["star5"] += 1

	# Inner loop end

	# Finding percentage value of positive and negative comments
	if review_count > 0:
		rating["pos"] = (pos*100)/review_count
		rating["neg"] = 100 - rating["pos"]
		# Normalizing the measures based on number of reviews
		rating["accurate"] /= review_count
		rating["ambience"] /= review_count
		rating["bake"] /= review_count
		rating["best"] /= review_count
		rating["commitment"] /= review_count
		rating["confidence"] /= review_count
		rating["delivery"] /= review_count
		rating["different"] /= review_count
		rating["economy"] /= review_count
		rating["enormous"] /= review_count
		rating["excellent"] /= review_count
		rating["fantastic"] /= review_count
		rating["filling"] /= review_count
		rating["flavor"] /= review_count
		rating["fresh"] /= review_count
		rating["friendly"] /= review_count
		rating["grow"] /= review_count
		rating["happy"] /= review_count
		rating["honest"] /= review_count
		rating["hot"] /= review_count
		rating["love"] /= review_count
		rating["memorable"] /= review_count
		rating["neighborhood"] /= review_count
		rating["new"] /= review_count
		rating["pleasant"] /= review_count
		rating["price"] /= review_count
		rating["quality"] /= review_count
		rating["quick"] /= review_count
		rating["reasonable"] /= review_count
		rating["recommend"] /= review_count
		rating["service"] /= review_count
		rating["special"] /= review_count
		rating["stuff"] /= review_count
		rating["sturdy"] /= review_count
		rating["surprise"] /= review_count
		rating["taste"] /= review_count
		rating["together"] /= review_count
		rating["worth"] /= review_count

	rating["address"] = business["full_address"] # Address of the business
	rating["city"] = business["city"] # Name of the city
	rating["state"] = business["state"] # Name of the city
	rating["stars"] = business["stars"] # Average stars for the business
	rating["name"] = business["name"] # Name of the business
	rating["categories"] = business["categories"] # All categories for the business

	# Append the created dictionary into a json file
	with open('model.json', 'a') as outfile:
		json.dump(rating, outfile)
		outfile.write("\n")

# End outer loop