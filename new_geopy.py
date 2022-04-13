from geopy.geocoders import Nominatim

# address we need to geocode
loc = 'narsapur, andhra pradesh'

# making an instance of Nominatim class
geolocator = Nominatim(user_agent="my_request")

# applying geocode method to get the location
location = geolocator.geocode(loc)

# printing address and coordinates
print(location.address)
#print((location.latitude, location.longitude))

#print(geolocator.reverse((location.latitude, location.longitude)).address)


#geolocator = Nominatim(user_agent="geoapiExercises")


def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    district= address.get("state_district"," ")
    state = address.get('state', '')
    country = address.get('country', '')
    pin=address.get("postcode")
    return city, district,state, country, pin


print(city_state_country((location.latitude,location.longitude)))
