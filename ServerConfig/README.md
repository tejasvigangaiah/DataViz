Yelp Visual Recommender - Server Code
=====================================

Usage
-----

- The server code should be used in this format to get the outputs - (https://yelp-reco-dv.herokuapp.com/recommend?location=Edinburgh&categories=Indian,Italian&preferences=ambience,quick,service)
- P.S. The format of query string passed is very important. 
- List of available locations - Phoenix, Madison, Las Vegas, Pittsburgh, Charolette, Urbana-Champaign, Waterloo, Montreal, Edinburgh, Karlsruhe
- List of categories - Try with possible restaurant types (Bars, Continental, Chinese etc.) P.S. - make it max 5 categories
- List of preferences - checkout the file 'Analysis/Lookup words.xlsx'. P.S. - The preferences should be in lower case

Analysis
--------

- This folder contains all the files used to create a model on the given data
- **Created Models**
  - This folder contains the models created from Yelp dataset
  - modelfinal.json was finally used as the model file
- **Sentiment Analysis**
  - This folder consists of a simple python code that returns polarity of a sentence using *Textblob* package
- **ModelCreation.py**
  - The file ModelCreation.py creates the model from MongoDB using all the lookup words (see 'Lookup words.xlsx')
  - This file performs sentiment analysis on all the reviews for a given business and assigns the polarity value to the corresponding lookup word if it appears on that review.
  - At every step, the model data is fed into the model.json file
- **MongoLabTest.py**
  - This is a simple test code for connecting to MongoLab database created from the model files

Heroku server files
-------------------

- This folder contains all the files that were used to deploy the application onto Heroku platform
- **Procfile** - This file is required for setting up how heroku platform behaves
- **recommend.py** - This file uses the database to return a set of recommended places based on location, categories and preferences
- **requirements.txt** - This file consists of all the packages required by heroku to execute the app