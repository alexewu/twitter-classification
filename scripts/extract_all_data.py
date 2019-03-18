# import tweepy
# from tweepy.auth import OAuthHandler
import json
from pprint import pprint
import time

# #access API
# auth = tweepy.OAuthHandler("w0MoZMRnilI3Nzvcn8pBf9V4g", "zkVujOFQphD8OChGCv7jAlrxZZ3Lus28vMeA4wM6HoIuI9Wlzn")
# auth.set_access_token("1088318072845492224-kiJEdhmm1cGY5gwgQdkiLDgJfsxUtp", "OhbRQIfANg3JxksuRq9ThujgjHHJY2oro4oTN1HLFl8UX")
#
# api = tweepy.API(auth)


# with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/posts/training-data.json") as f:
#     data = json.load(f)
#
# #EXRACT ALL DATA
# all = data['events']
#
# # #create a dict each element contains event id and post info
# all_data = []
# numErrorPosts = 0
# numNormalPosts = 0
#
# for event in all:
#     index = 0
#     for tweet in event["tweets"]:
# 	 content = {}
# 	     content['eventid'] = event["eventid"]
# 	     content["postID"] = tweet["postID"]
# 	     content["categories"] = tweet["categories"]
# 	     content["indicatorTerms"] = tweet["indicatorTerms"]
# 	     content["priority"] = tweet["priority"]
# 	     all_data.append(content)
# 	     index += 1
# 		  try:
# 		      tweet = api.get_status(tweet['postID'])
# 		      content["content"] = tweet.text
# 		      numNormalPosts += 1
# 			   except tweepy.TweepError:
# 				numErrorPosts += 1
# 				    content["content"] = "Error"
# 				    print("Failed to get info on", tweet['postID'], "....Skipping...") #do not include this information in JSON data
# 				print("going into sleep mode")
#     time.sleep(600)
#
#
# # print("Number of posts that failed to load: ", numErrorPosts)
# # print("Got", numNormalPosts, "posts")
#
# with open('/Users/alexandrawu/Desktop/twitter2/venv/all-with-posts.json', 'w') as outfile:
#     json.dump(all_data, outfile, indent=4)

with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/10-test.json") as f:
    data = json.load(f)

no_error = []
counter = 0
for element in data:
	if element["content"] != "Error":
		no_error.append(element)

with open('/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/10-test-no-error.json', 'w') as outfile:
	json.dump(no_error, outfile, indent=4)

