import json

#result = [json.loads(jline) for jline in jsonl_content.split('\n')]

with open("/Users/alexandrawu/Desktop/twitter-categorizer/tweet-sample.jsonl") as f:
    for line in f:
        j_content = json.loads(line)
        print(j_content['text'])
