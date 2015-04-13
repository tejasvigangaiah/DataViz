from textblob import TextBlob

text = "great. awesome but can be better. I really like how things end in this. lets see. it should be good"
blob = TextBlob(text)

#for sentence in blob.sentences:
    #print(sentence.sentiment.polarity)
print(blob.sentiment.polarity)
