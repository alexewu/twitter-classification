import tweepy
import json
from pprint import pprint

#access API
auth = tweepy.OAuthHandler("w0MoZMRnilI3Nzvcn8pBf9V4g", "zkVujOFQphD8OChGCv7jAlrxZZ3Lus28vMeA4wM6HoIuI9Wlzn")
auth.set_access_token("1088318072845492224-kiJEdhmm1cGY5gwgQdkiLDgJfsxUtp", "OhbRQIfANg3JxksuRq9ThujgjHHJY2oro4oTN1HLFl8UX")

api = tweepy.API(auth)


with open("/Users/alexandrawu/Desktop/twitter-categorizer/training-data.json") as f:
    data = json.load(f)

# #fireColorado posts
event = data['events'][2]['tweets']

# #create a dict key=postID and value=postContents
numErrorPosts = 0
numNormalPosts = 0

for post in event:
    # tweet = api.get_status(post['postID'])
    # print(tweet.text)
    try:
        tweet = api.get_status(post['postID'])
        numNormalPosts += 1
    except tweepy.TweepError:
        numErrorPosts += 1
        print("Failed to get info on", post['postID'], "....Skipping...") #do not include this information in JSON data

print("Number of posts that failed to load: ", numErrorPosts)
print("Got", numNormalPosts, "posts to load")

