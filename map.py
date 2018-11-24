# returns relevant Google Maps data based on user-input location

import requests
import json

api_key = "AIzaSyClKuWY2YUpxRL_ypzI6CcN-U6KDjtHinY"
  
# url variable store url 
urlgeo 	  = "https://maps.googleapis.com/maps/api/geocode/json?"
urlplaces = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=44.2253,-76.4951&radius=5000&type=restaurant&keyword=pizza&key=AIzaSyBF4V3_kp1x6Y6Ovalq4bmWfyokh_edgk4"

# user input of place string, this will be changed to the user input on the website
address_string = "Queen's University"

# requests relevant information from the Google Maps server
rgeo = requests.get(urlgeo + "address=" + address_string + "&key=" + api_key)
fgeo = open('latlong.txt', 'wb')
fgeo.write(rgeo.content)
fgeo = open('latlong.txt', 'r')

# parses the latitude and longitude information from Google Maps
geo_json = json.load(fgeo)
loc_lat  = geo_json["lat"]["geometry"]["location"]["lat"]
loc_lng  = geo_json["results"]["geometry"]["location"]["lng"]

places = requests.get(urlplaces)

# opens the files it will write this information to, and subsequently writes to them
fplaces = open('pizzaplaces.txt', 'wb')
floc = open('locs.txt', 'wb')
#fplaces.write(rplaces.content)

#floc.write(loc_lng)
#fplaces.write(loc_lat)

# closes the image file it wrote to
fgeo.close()
fplaces.close()
