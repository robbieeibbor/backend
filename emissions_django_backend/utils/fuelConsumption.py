from datetime import datetime
from math import radians, sin, cos, sqrt, atan2

# haversine formula with some assistance from https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
#this should have been combined into one haversine formula and used for botht journey distance and fuel consumption
def haversineFuel(lat1, lon1, lat2, lon2):
    earthRadius= 6371  # radius of the Earth

    # converts lat/long from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [float(lat1), float(lon1), float(lat2), float(lon2)])

    # haversine formula
    diffLat = lat2 - lat1
    diffLon = lon2 - lon1
    a = sin(diffLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(diffLon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #distance (km)
    distanceKm = earthRadius* c 
    #convert to nautical miles
    distance = distanceKm * 0.53996 
    #this returns distance as nautical miles
    return distance

def calculate_speed_time_fuel(data):
    speeds = []
    times = []
    fuel_consumption = []
    fuel_consumed = []

    for i in range(1, len(data)):
        lat1, lon1 = data[i - 1]['latitude'], data[i - 1]['longitude']
        lat2, lon2 = data[i]['latitude'], data[i]['longitude']
        timestamp1 = datetime.fromisoformat(data[i - 1]['message_timestamp'])
        timestamp2 = datetime.fromisoformat(data[i]['message_timestamp'])

        # calc distance
        distance = haversineFuel(lat1, lon1, lat2, lon2)
        print('distance is ', distance)
        print('timestamp 1 ', timestamp1)
        print('timestamp 2 ', timestamp2)
        # calculate time difference(hours)
        time_difference = (timestamp2 - timestamp1).total_seconds() / (24 * 60 * 60)
        print('time diff is ', time_difference)
        # calculate speed (knots)
        time_difference_hours = 24*time_difference
        speed = distance / time_difference_hours
        print("speed ",speed)

        print("\n\ni\n",i)

        speeds.append(speed)
        times.append(time_difference)

        rounded_speed = round(speed)
        # estimate the fuel consumption based on thespeed, fuel consumption is per day
        if  rounded_speed == 0:
            fuel_consumption.append(0)
        elif rounded_speed <= 12:
            fuel_consumption.append(87.5)
        elif rounded_speed == 13:
            fuel_consumption.append(90)
        elif rounded_speed == 14:
            fuel_consumption.append(92.5)
        elif rounded_speed == 15:
            fuel_consumption.append(95)
        elif rounded_speed == 16:
            fuel_consumption.append(97.5)
        elif rounded_speed == 17:
            fuel_consumption.append(100)
        elif rounded_speed ==18:
            fuel_consumption.append(125)
        elif rounded_speed ==19:
            fuel_consumption.append(150)
        elif rounded_speed ==20:
            fuel_consumption.append(175)
        elif rounded_speed ==21:
            fuel_consumption.append(200)
        elif rounded_speed ==22:
            fuel_consumption.append(235)
        elif rounded_speed ==23:
            fuel_consumption.append(255)
        elif rounded_speed ==24:
            fuel_consumption.append(320)
        elif rounded_speed ==24:
            fuel_consumption.append(330)
        elif rounded_speed >= 25:
            fuel_consumption.append(360)
        
    fuel_consumed = [time * fuel for time, fuel in zip(times, fuel_consumption)]
    print("fuel consumed ",fuel_consumed)
    total_fuel_consumed = sum(fuel_consumed)
    # we are using an emissions factor of 3.151 tons of carbon emitted for every ton opf fuel burned
    co2_emissions = total_fuel_consumed * 3.151
    print(co2_emissions)

    response = {
        "speeds": speeds,
        "times_in_days": times,
        "fuel_consumption": fuel_consumption,
        "fuel_consumed": fuel_consumed,
        "total_fuel_consumed": total_fuel_consumed,
        "co2_emissions": co2_emissions
    }

    print("times \n\n",times,"\n\n")

    print("speeds \n\n",speeds,"\n\n")

    print("fuel CONSUMPTION \n\n",fuel_consumption,"\n\n")

    print("fuel consumed \n\n",fuel_consumed,"\n\n")

    return response

