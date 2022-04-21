from geopy.geocoders import GoogleV3

point = '51.523910, -0.158578'
geocoder = GoogleV3(api_key="", domain='maps.googleapis.com',
                    user_agent="project1")
address = geocoder.reverse(point)


