# geocoding_techniques using open street map (osm) open source library
import geocoder

g = geocoder.osm(input("please enter address"), user_agent="my-task")


# function which returns city district state country pin fields
def city_state_country(address):
    address = address
    city = address["city"]
    district = address["state_district"]
    state = address["state"]
    country = address["state"]
    pin = address["postcode"]
    return city, district, state, country, pin


print(g.raw["address"])
print(city_state_country(g.raw["address"]))
