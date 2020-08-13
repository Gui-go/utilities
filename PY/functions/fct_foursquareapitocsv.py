#!/usr/bin/env python3

# Import needed packages
import json
import requests
import csv
import re
import pandas as pd

# Documentation
'https://developer.foursquare.com/'
'https://developer.foursquare.com/docs/places-api/getting-started/'


# Defining function
def getPlaces(CLIENT_ID, CLIENT_SECRET, LAT, LNG, QUERY, LIMIT, VERIFIED='Null'):
    
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
    filtered_columns = ['venue.id', 'venue.name', 'venue.location.address', 'venue.location.lat', 'venue.location.lng', 'venue.location.distance', 'venue.location.city', 'venue.location.state', 'venue.location.country', 'venue.location.formattedAddress', 'venue.categories', 'venue.verified', 'venue.location.postalCode', 'venue.location.neighborhood']
    nearby_venues = nearby_venues.loc[:, filtered_columns]

    # Rename columns
    nearby_venues.columns = ['id', 'name', 'address', 'lat', 'lng', 'distance_from_search', 'city', 'state', 'country', 'formattedAddress', 'categories', 'verified', 'postalCode', 'neighborhood']

    # Getting only the name of the cotegory
    for i in range(0, len(nearby_venues.categories)):
        nearby_venues.categories[i] = re.search("'name': '(.*)', 'pluralName'", str(nearby_venues.categories[i])).group(1)

    # Reordering the dataframe
    df = nearby_venues[['id', 'name', 'lat', 'lng', 'neighborhood', 'city', 'state', 'country', 'address', 'formattedAddress', 'postalCode', 'distance_from_search', 'categories', 'verified']]

    # Convert it all to string
    df = df.astype(str)

    # if VERIFIED == True => filter; else do nothing
    if VERIFIED=='True': 
        df = df[df['verified']=='True']

    # Return df
    return df

# Call function
places = getPlaces(
    CLIENT_ID = "52ORGP3WX1HNQCYIQRTNZB052HDR4BXEHR3YEHWPFAQRF2GS",
    CLIENT_SECRET = "P3J31D55BNMW4MY2PMH5GW4QTZ5KMIPKDCI2LEPHXKBVFPKX",
    LAT = -23.556439,
    LNG = -46.605931,
    QUERY='Shopping mall',
    LIMIT=30#,
    #VERIFIED='True'
)


places
places.name

# places.to_csv(r'locations.csv', index = False)