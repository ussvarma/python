from geopy.geocoders import Nominatim

# address we need to geocode
loc = input("please enter the address")

# making an instance of Nominatim class
geolocator = Nominatim(user_agent="my_req")

# applying geocode method to get the location
location_coordinates = geolocator.geocode(loc)


def city_state_country(coord):
    # function which returns address fields
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    district = address.get("state_district", " ")
    state = address.get('state', '')
    country = address.get('country', '')
    pin = address.get("postcode")
    return city, district, state, country, pin


print(city_state_country((location_coordinates.latitude, location_coordinates.longitude)))
