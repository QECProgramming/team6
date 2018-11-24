# returns relevant Google Maps data based on user-input location

import requests, json

api_key = "AIzaSyClKuWY2YUpxRL_ypzI6CcN-U6KDjtHinY"

# url variable store url
urlgeo 	  = "https://maps.googleapis.com/maps/api/geocode/json?"
urlplaces = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

# user input of place string, this will be changed to the user input on the website
address_string = input("Input the location you're shopping for pizza in (Exact locations and general areas are both acceptable).")

# requests relevant latitude and longitude information from the Google Maps server
rgeo = requests.get(urlgeo + "address=" + address_string + "&key=" + api_key)
fgeo = open('latlong.txt', 'wb')
fgeo.write(rgeo.content)
fgeo = open('latlong.txt', 'r')

# parses the latitude and longitude information from Google Maps
geo_json = json.load(fgeo)
loc_lat  = geo_json["results"][0]["geometry"]["location"]["lat"]
loc_lng  = geo_json["results"][0]["geometry"]["location"]["lng"]

print ("This location's latitude is " + str(loc_lat))
print ("This location's longitude is " + str(loc_lng))

# requests relevant pizza restaurant information from Google Maps
rplaces = requests.get(urlplaces + "location=" + str(loc_lat) + "," + str(loc_lng) + "&radius=5000&type=restaurant&keyword=pizza&key=" + api_key)

# opens the restaurant file it will write this information to and subsequently writes to it
fplaces = open('pizzaplaces.txt', 'wb')
fplaces.write(rplaces.content)
fplaces = open('pizzaplaces.txt', 'r')

# parses the restaurant names from Google Maps, puts them to an array and prints them off
places_json = json.load(fplaces)
res_places = []
for i in range(0, 10):
    res_places.append(places_json["results"][i]["name"])

print ("The pizza restaurants in a 5km radius from your location are:")
print (res_places)

# closes the image file it wrote to
fgeo.close()
fplaces.close()

wait = input("PRESS ENTER TO EXIT.")