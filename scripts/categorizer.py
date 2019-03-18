import spacy
import json
nlp = spacy.load('en')

with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/80-no-error.json") as f:
    data = json.load(f)

train_data = []
for post in data:
    priority = {}
    if post["priority"] == "Low":
        priority = {"cats": {"Low": 1, "Medium": 0, "High": 0}}
    elif post["priority"] == "Medium":
        priority = {"cats": {"Low": 0, "Medium": 1, "High": 0}}
    else:
        priority = {"cats": {"Low": 0, "Medium": 0, "High": 1}}
    pair = (post["content"], priority)
    train_data.append(pair)


textcat = nlp.create_pipe('textcat')
nlp.add_pipe(textcat, last=True)
textcat.add_label('Low')
textcat.add_label('Medium')
textcat.add_label('High')
optimizer = nlp.begin_training()
for itn in range(10):
    for doc, gold in train_data:
        nlp.update([doc], [gold], sgd=optimizer)


with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/10-dev-no-error.json") as f:
    test_data = json.load(f)

num_correct = 0
num_total = 0
output = []
for post in test_data:
    doc = nlp(post["content"])
    print(doc.cats)
    result = doc.cats
    output.append(result)
    num_total += 1
    maxValue = max(result.values())
    maxPriority = [k for k,v in result.items() if v == maxValue]
    if maxPriority[0] == post["priority"]:
        num_correct += 1


print("The number of correctly categorized posts is %d out of %d" % (num_correct, num_total))
print("The percent correctly calculated is %f" % (float(num_correct) / num_total))

with open('/Users/alexandrawu/Desktop/twitter2/ratings.json', 'w') as outfile:
    json.dump(output, outfile, indent=4)





