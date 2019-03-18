import json
from pprint import pprint

with open("/Users/alexandrawu/Desktop/twitter2/ratings.json") as f:
    ratings = json.load(f)

with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/10-dev-no-error.json") as f:
    posts = json.load(f)


#get counts for low priority
low = 0
medium = 0
high = 0
counter = 0
for post in posts:
    if post["priority"] == "Low":
        maxValue = max(ratings[counter].values())
        maxPriority = [k for k,v in ratings[counter].items() if v == maxValue]
        if maxPriority[0] == "Low":
            low += 1
        elif maxPriority[0] == "Medium":
            medium += 1
        else:
            high += 1
    counter += 1
    #print(counter)

print("%d %d %d\n" % (low, medium, high))

#get counts for medium priority
low = 0
medium = 0
high = 0
counter = 0

for post in posts:
    if post["priority"] == "Medium":
        maxValue = max(ratings[counter].values())
        maxPriority = [k for k,v in ratings[counter].items() if v == maxValue]
        if maxPriority[0] == "Low":
            low += 1
        elif maxPriority[0] == "Medium":
            medium += 1
        else:
            high += 1
    counter += 1

print("%d %d %d\n" % (low, medium, high))

#get counts for high priority
low = 0
medium = 0
high = 0
counter = 0

for post in posts:
    if post["priority"] == "High":
        maxValue = max(ratings[counter].values())
        maxPriority = [k for k,v in ratings[counter].items() if v == maxValue]
        if maxPriority[0] == "Low":
            low += 1
        elif maxPriority[0] == "Medium":
            medium += 1
        else:
            high += 1
    counter += 1

print("%d %d %d\n" % (low, medium, high))
