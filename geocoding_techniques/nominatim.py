# using nominatim
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example app")

# gives latitudes and longitudes
geo_info = geolocator.geocode(input("please enter details")).point

# reverse gecoding
print(geolocator.reverse(geo_info))
