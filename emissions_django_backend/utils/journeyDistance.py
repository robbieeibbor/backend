from math import radians, sin, cos, sqrt, atan2

#haversine formula with some assistance from https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
#this should have been combined into one haversine formula and used for botht journey distance and fuel consumption
def haversine(lat1, lon1, lat2, lon2):
    #convert lat/longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [float(lat1), float(lon1), float(lat2), float(lon2)])

    #haversine formula
    diffLat = lat2 - lat1
    diffLon = lon2 - lon1
    a = sin(diffLat / 2)**2 + cos(lat1) * cos(lat2) * sin(diffLon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    #adius of earth in km // needs to be converted to nm! 
    earthRadius = 6371.0

    #calculate distance
    distance = earthRadius * c
    #distance here is returned as km, this needs to be converted
    return distance

def calculate_journey_distance(journey_data, unit='km'):
    total_distance = 0.0
     #1 nautical mile(nm)= 1.852 kilometers
    conversion_factor = 1.852 

    for i in range(len(journey_data) - 1):
        current_point = journey_data[i]
        next_point = journey_data[i + 1]

        distance = haversine(
            current_point['latitude'],
            current_point['longitude'],
            next_point['latitude'],
            next_point['longitude']
        )

        total_distance += distance

    if unit.lower() == 'nm':
        #converts total distance to nautical miles
        total_distance /= conversion_factor

    return total_distance

