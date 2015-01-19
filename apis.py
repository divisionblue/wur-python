import requests

with open('cities.txt', 'r') as cities:
    results = []
    for city in cities:
        query = city.strip()
        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?"
                         "address={}".format(query))
        location = r.json()['results'][0]['geometry']['location']
        results.append({"city": query, "latlng": location})

print results
