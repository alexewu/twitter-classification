import json
from pprint import pprint

with open("/Users/alexandrawu/Desktop/twitter-categorizer/costaRicaEarthquake2012.json") as f:
    data = json.load(f)

pprint(data)

#how to dump data prettily into JSON file?
