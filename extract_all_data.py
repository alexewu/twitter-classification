import tweepy
from tweepy.auth import OAuthHandler
import json
from pprint import pprint

#access API
auth = tweepy.OAuthHandler("w0MoZMRnilI3Nzvcn8pBf9V4g", "zkVujOFQphD8OChGCv7jAlrxZZ3Lus28vMeA4wM6HoIuI9Wlzn")
auth.set_access_token("1088318072845492224-kiJEdhmm1cGY5gwgQdkiLDgJfsxUtp", "OhbRQIfANg3JxksuRq9ThujgjHHJY2oro4oTN1HLFl8UX")

api = tweepy.API(auth)


with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/posts/training-data.json") as f:
    data = json.load(f)

#EXRACT ALL DATA
all = data['events']

# #create a dict each element contains event id and post info
all_data = []
numErrorPosts = 0
numNormalPosts = 0

# for event in all:
#     event_dict = {}
#     event_dict["eventid"] = event["eventid"]
#     tweets = []
#     index = 0
#     for tweet in event["tweets"]:
#         content = {}
#         content["postID"] = tweet["postID"]
#         content["categories"] = tweet["categories"]
#         content["indicatorTerms"] = tweet["indicatorTerms"]
#         content["priority"] = tweet["priority"]
#         tweets.append(content)
#         index += 1
#         try:
#             tweet = api.get_status(tweet['postID'])
#             content["content"] = tweet.text
#             numNormalPosts += 1
#         except tweepy.TweepError:
#             numErrorPosts += 1
#             print("Failed to get info on", tweet['postID'], "....Skipping...") #do not include this information in JSON data
#     event_dict["tweets"] = tweets
#     all_data.append(event_dict)

event_dict = {}
event_dict["eventid"] = "laShooting"
tweets = []
for tweet in all[4]["tweets"]:
        content = {}
        content["postID"] = tweet["postID"]
        content["categories"] = tweet["categories"]
        content["indicatorTerms"] = tweet["indicatorTerms"]
        content["priority"] = tweet["priority"]
        tweets.append(content)
        try:
            tweet = api.get_status(tweet['postID'])
            content["content"] = tweet.text
            numNormalPosts += 1
        except tweepy.TweepError:
            numErrorPosts += 1
            print("Failed to get info on", tweet['postID'], "....Skipping...") #do not include this information in JSON data
event_dict["tweets"] = tweets


# print("Number of posts that failed to load: ", numErrorPosts)
# print("Got", numNormalPosts, "posts")
#
# print("\nTweets in", data['events'][5]['eventid'], ":")
# for key, value in event_data.items():
#     print(key, ':', value)
with open('/Users/alexandrawu/Desktop/twitter/la_shooting_with_content.json', 'w') as outfile:
    json.dump(event_dict, outfile, indent=4)

