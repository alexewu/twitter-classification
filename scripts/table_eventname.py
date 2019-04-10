import json
from pprint import pprint

#input in a string of the gold event name
def get_row(gold, ratings, posts):
    #get counts for low priority
    costaRica = 0
    fireColorado = 0
    floodColorado = 0
    typhoonPablo = 0
    laAirport = 0
    westTexas = 0
    counter = 0
    for post in posts:
        if post["eventid"] == gold:
            maxValue = max(ratings[counter].values())
            maxPriority = [k for k,v in ratings[counter].items() if v == maxValue]
            if maxPriority[0] == "costaRicaEarthquake2012":
                costaRica += 1
            elif maxPriority[0] == "fireColorado2012":
                fireColorado += 1
            elif maxPriority[0] == "floodColorado2013":
                floodColorado += 1
            elif maxPriority[0] == "typhoonPablo2012":
                typhoonPablo += 1
            elif maxPriority[0] == "laAirportShooting2013":
                laAirport += 1
            elif maxPriority[0] == "westTexasExplosion2013":
                westTexas += 1
        counter += 1
        #print(counter)
    print("%d %d %d %d %d %d\n" % (costaRica, fireColorado, floodColorado, typhoonPablo, laAirport, westTexas))

if __name__ == '__main__':
    with open("/Users/michelle02px2017/PycharmProjects/twitter/rating.json") as f:
        ratings = json.load(f)

    with open("/Users/michelle02px2017/Desktop/twitter2/venv/twitter-classification/all-posts/10-dev.json") as f:
        posts = json.load(f)

    event_names = ["costaRicaEarthquake2012", "fireColorado2012", "floodColorado2013", "typhoonPablo2012", "laAirportShooting2013", "westTexasExplosion2013"]

    for event in event_names:
        get_row(event, ratings, posts)
