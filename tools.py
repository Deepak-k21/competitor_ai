import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.getenv("AIzaSyC8-ebHoP7bJ0Xjzkou33JEte05ojtx0do"))

def search_clothing_stores(location):
    results = gmaps.places(query=f"clothing stores in {location}")
    
    stores = []
    for place in results['results'][:5]:
        stores.append({
            "name": place['name'],
            "rating": place.get('rating', 'N/A'),
            "reviews": place.get('user_ratings_total', 0),
            "address": place.get('formatted_address', 'N/A')
        })
    return stores