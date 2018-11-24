# returns relevant Google Maps data based on user-input location

import requests
import json

api_key = "AIzaSyClKuWY2YUpxRL_ypzI6CcN-U6KDjtHinY"
  
# url variable store url 
urlgeo 	  = "https://maps.googleapis.com/maps/api/geocode/json?"
urlplaces = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

# user input of place string, this will be changed to the user input on the website
address_string = "Queen's University"

# requests relevant latitude and longitude information from the Google Maps server
rgeo = requests.get(urlgeo + "address=" + address_string + "&key=" + api_key)
fgeo = open('latlong.txt', 'wb')
fgeo.write(rgeo.content)
fgeo = open('latlong.txt', 'r')

# parses the latitude and longitude information from Google Maps
geo_json = json.load(fgeo)
loc_lat  = geo_json["results"][0]["geometry"]["location"]["lat"]
loc_lng  = geo_json["results"][0]["geometry"]["location"]["lng"]

# requests relevant pizza restaurant information from Google Maps
rplaces = requests.get(urlplaces + "location=" + str(loc_lat) + "," + str(loc_lng) + "&radius=5000&type=restaurant&keyword=pizza&key=" + api_key)

# opens the restaurant file it will write this information to and subsequently writes to it
fplaces = open('pizzaplaces.txt', 'wb')
fplaces.write(rplaces.content)
fplaces = open('pizzaplaces.txt', 'r')

# parses the restaurant names from Google Maps
places_json = json.load(fplaces)
loc_lat  = geo_json["results"][0]["geometry"]["location"]["lat"]
loc_lng  = geo_json["results"][0]["geometry"]["location"]["lng"]

# closes the image file it wrote to
fgeo.close()
fplaces.close()
