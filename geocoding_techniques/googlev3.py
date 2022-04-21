from geopy.geocoders import GoogleV3

point = '51.523910, -0.158578'
geocoder = GoogleV3(api_key="AIzaSyA5lJQXfAh8EKfHuIypna9im1F_OFMXDIk", domain='maps.googleapis.com',
                    user_agent="project1")
address = geocoder.reverse(point)


