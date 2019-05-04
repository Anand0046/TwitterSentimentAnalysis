#Building the dataset for project

def build_rest_set_data(searchhashtag):
    try:
        tweets_fetched = twitter_api.GetSearch(searchhashtag, count = 100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + searchhashtag)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Tweets not found")
        return None
