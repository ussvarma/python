# importing libraries
import geocoder


def find_lat_long(given_address):
    # function which returns latitude and longitudes
    g = geocoder.google(given_address, KEY="")  # api key is a paid service
    lat_long = g.latlng
    return lat_long


def address_details(lat_long):
    # function which returns city, country,pincode
    g = geocoder.google(lat_long, method="reverse", KEY='')
    return g.city, g.country, g.postal


lat_long_coordinates = find_lat_long(input("please enter the address:"))
print(address_details(lat_long_coordinates))
