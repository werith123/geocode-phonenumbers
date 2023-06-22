import phonenumbers
import folium
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

# Replace 'number' with the actual phone number you want to geocode
number = "<phone_number>"

# Replace 'lat' and 'lng' with the desired latitude and longitude values
lat = 37.7749
lng = -122.4194

# Replace 'API_KEY' with your actual OpenCage API key
API_KEY = 'da4c482990db45aca23a3e73dd9d3743'

# Get the location description for the phone number
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)

# Create an instance of the OpenCageGeocode with your API key
geocoder = OpenCageGeocode(API_KEY)

# Create a query string with the location description
query = yourLocation

# Geocode the location using OpenCageGeocode
results = geocoder.geocode(query)

# Extract latitude and longitude from the geocoding results
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Create a folium map centered around the geocoded location
myMap = folium.Map(location=[lat, lng], zoom_start=9)

# Add a marker to the map with the location description
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# Save the map to an HTML file
myMap.save("myLocation.html")


