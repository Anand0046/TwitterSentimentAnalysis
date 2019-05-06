def buidTraining_DataSet(DataFile, tweet_DataFile):
    import csv
    import time
    #taking sentence from file and seperating it.
    data = []
    
    with open(DataFile,'rb') as csvfile:
        line_reader = csv.reader(csvfile,delimiter=',', quotechar="\"")
        for row in line_reader:
            data.append({"tweet_id":row[2], "label":row[1], "topic":row[0]})
            
    rate_limit = 200
    sleep_time = 900/200
    
    training_data_set = []
    
    for tweet in data:
        try:
            status = twitter_api.GetStatus(tweet["tweet_id"])
            print("Tweet fetched" + status.text)
            tweet["text"] = status.text
            training_data_set.append(tweet)
            time.sleep(sleep_time) 
        except: 
            continue
    # writing to an empty csv file
    with open(tweet_DataFile,'wb') as csvfile:
        linewriter = csv.writer(csvfile,delimiter=',',quotechar="\"")
        for tweet in training_data_set:
            try:
                linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
            except Exception as e:
                print(e)
    return training_data_set
