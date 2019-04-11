import spacy
import json
nlp = spacy.load('en')

#loading the training data
with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/training-data/40-training.json") as f:
    data = json.load(f)

train_data = []
for post in data:
    priority = {}
    if post["eventid"] == "costaRicaEarthquake2012":
        priority = {"cats": {"costaRicaEarthquake2012": 1, "fireColorado2012": 0, "floodColorado2013": 0, "typhoonPablo2012": 0, "laAirportShooting2013": 0, "westTexasExplosion2013": 0}}
    elif post["eventid"] == "fireColorado2012":
        priority = {"cats": {"costaRicaEarthquake2012": 0, "fireColorado2012": 1, "floodColorado2013": 0, "typhoonPablo2012": 0, "laAirportShooting2013": 0, "westTexasExplosion2013": 0}}
    elif post["eventid"] == "floodColorado2013":
        priority = {"cats": {"costaRicaEarthquake2012": 0, "fireColorado2012": 0, "floodColorado2013": 1, "typhoonPablo2012": 0, "laAirportShooting2013": 0, "westTexasExplosion2013": 0}}
    elif post["eventid"] == "typhoonPablo2012":
        priority = {"cats": {"costaRicaEarthquake2012": 0, "fireColorado2012": 0, "floodColorado2013": 0, "typhoonPablo2012": 1, "laAirportShooting2013": 0, "westTexasExplosion2013": 0}}
    elif post["eventid"] == "laAirportShooting2013":
        priority = {"cats": {"costaRicaEarthquake2012": 0, "fireColorado2012": 0, "floodColorado2013": 0, "typhoonPablo2012": 0, "laAirportShooting2013": 1, "westTexasExplosion2013": 0}}
    elif post["eventid"] == "westTexasExplosion2013":
        priority = {"cats": {"costaRicaEarthquake2012": 0, "fireColorado2012": 0, "floodColorado2013": 0, "typhoonPablo2012": 0, "laAirportShooting2013": 0, "westTexasExplosion2013": 1}}
    pair = (post["content"], priority)
    train_data.append(pair)


textcat = nlp.create_pipe('textcat')
nlp.add_pipe(textcat, last=True)
textcat.add_label('costaRicaEarthquake2012')
textcat.add_label('fireColorado2012')
textcat.add_label('floodColorado2013')
textcat.add_label('typhoonPablo2012')
textcat.add_label('laAirportShooting2013')
textcat.add_label('westTexasExplosion2013')
optimizer = nlp.begin_training()
for itn in range(10):
    for doc, gold in train_data:
        nlp.update([doc], [gold], sgd=optimizer)


with open("/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/10-dev.json") as f:
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
    if maxPriority[0] == post["eventid"]:
        num_correct += 1


print("The number of correctly categorized posts is %d out of %d" % (num_correct, num_total))
print("The percent correctly calculated is %f" % (float(num_correct) / num_total))

with open('/Users/alexandrawu/Desktop/twitter2/venv/twitter-classification/all-posts/ratings.json', 'w') as outfile:
    json.dump(output, outfile, indent=4)





