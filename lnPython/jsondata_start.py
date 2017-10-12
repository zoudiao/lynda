import urllib2
import json

def printResults(data):
    theJSON = json.load(data)


    if "title" in theJSON["matadata"]:
        print theJSON["metadata"]["title"]

def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if(webUrl.getcode==200):
        data = webUrl.read()
        printResults(data)
    else:
        print "Received an error from server, can't retrieve results" + str(webUrl.getcode)

if __name__ == '__main__':
    main()
