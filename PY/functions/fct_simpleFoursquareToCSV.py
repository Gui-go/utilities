#!/usr/bin/env python3

# Import needed packages
import json
import requests
import csv
import re
import pandas as pd

# Documentation
# 'https://developer.foursquare.com/'
# 'https://developer.foursquare.com/docs/places-api/getting-started/'

# Defining function
def getPlaces(CLIENT_ID, CLIENT_SECRET, LAT, LNG, QUERY, LIMIT=100, VERIFIED='Null'):

    # Parameters for request
    url = 'https://api.foursquare.com/v2/venues/explore'
    LL = str(LAT) + ' ,' + str(LNG)
    params = dict(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        v='20180323',
        ll=LL,
        query=QUERY,
        limit=LIMIT
    )

    # Requesting data
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    # Funneling JSON
    venues = data['response']['groups'][0]['items']

    # JSON to Tabular form
    nearby_venues = pd.json_normalize(venues)

    # filter columns
    filtered_columns = ['venue.name', 'venue.location.lat', 'venue.location.lng',
                        'venue.location.formattedAddress', 'venue.categories']
    nearby_venues = nearby_venues.loc[:, filtered_columns]

    # Rename columns
    nearby_venues.columns = ['name', 'lat', 'lng', 'formattedAddress', 'categories']

    # Getting only the name of the cotegory
    for i in range(0, len(nearby_venues.categories)):
        nearby_venues.categories[i] = re.search(
            "'name': '(.*)', 'pluralName'", str(nearby_venues.categories[i])).group(1)

    # Convert it all to string
    df = nearby_venues.astype(str)

    # Return df
    return df

if __name__ == '__main__':
    QUERY = input('Procurando por: ')
    places = getPlaces(
        CLIENT_ID="52ORGP3WX1HNQCYIQRTNZB052HDR4BXEHR3YEHWPFAQRF2GS",
        CLIENT_SECRET="P3J31D55BNMW4MY2PMH5GW4QTZ5KMIPKDCI2LEPHXKBVFPKX",
        LAT=-27.614250,
        LNG=-48.643154,
        QUERY=QUERY,
        LIMIT=30#,
        # VERIFIED='True'
    )
    print(places)
