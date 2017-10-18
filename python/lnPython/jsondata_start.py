import urllib2
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]


    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]


    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if(feltReports != None) & (feltReports>0):
            print "%2.1f" %i["properties"]["mag"],i["properties"]["place"], " reported" + str(feltReports) + " times"
def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"

    # open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()

    if( webUrl.getcode() == 200 ):
        data = webUrl.read()
        printResults(data)
    else:
        print "Received an error from server, can't retrieve results" + str(webUrl.getcode)

if __name__ == '__main__':
    main()
