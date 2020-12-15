"""
@author: Payal Patel
Python Assignment 1: Dark Sky Weather Forecast 

"""
#import packages/libraries
import numpy as np
import pandas as pd
import os
from forecastiopy import * 

#get and print current working directory 
#cwd = os.getcwd()
#print(cwd)

#change working directory to PythonHW1 folder
os.chdir('C:/Users/19197/Documents/PythonHW1')
cwd = os.getcwd()
#print(cwd)

#store api in api_key variable
api_key = 'dabdb48c5e3db40144dd3586921cbdbd'

#create empty temp DataFrame with necessary columns
#temp DataFrame will be used later to add Min1-5, Max1-5, AvgMin, AvgMax variables for each city 
col_names =  ['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2', 'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min 5', 'Max 5', 'Min Avg', 'Max Avg']
temp  = pd.DataFrame(columns = col_names)

#view structure of Temp DataFrame
#str(temp)

#create loc list of lists - each list contains the latitude & longitude for a specific city 
loc = [\
       [ "Anchorage, Alaska", 61.2181, -149.9003 ],\
       [ "Buenos Aires, Argentia", -34.6037, -58.3816 ],\
       [ "Sao Jose dos Campos, Brazil", -23.2237, -45.9009 ],\
       [ "San Jose, Costa Rica", 9.9281, -84.0907 ],\
       [ "Nanaimo, Canada", 49.1659, -123.9401 ],\
       [ "Ningbo, China", 29.8683, 121.5440 ],\
       [ "Giza, Egypt", 30.0131, 31.2089 ],\
       [ "Mannheim, Germany", 49.4875, 8.4660 ],\
       [ "Hyderabad, India", 17.3850, 78.4867 ],\
       [ "Tehran, Iran", 35.6892, 51.3890 ],\
       [ "Bishkek, Kyrgyzstan", 42.8746, 74.5698 ],\
       [ "Riga, Latvia", 56.9496, 24.1052 ],\
       [ "Quetta, Pakistan", 30.1798, 66.9750 ],\
       [ "Warsaw, Poland", 52.2297, 21.0122 ],\
       [ "Dhahran, Saudia Arabia", 26.2361, 50.0393 ],\
       [ "Madrid, Spain", 40.4168, -3.7038 ],\
       [ "Oldham, United Kingdom", 53.5409, -2.1114 ],\
]

#create empty list, newRow (to be used in for loop)
newRow = []

for location in loc:
    #store city, latitude, and longitude for current location in loop into the city, lat, and lon variables respectively
    city = location[0]
    lat = location[1]
    lon = location[2]
    #pull data from Dark Sky using API for current location in for loop
    weather = ForecastIO.ForecastIO( api_key, latitude=lat, longitude=lon, units = 'si')
    current = FIOCurrently.FIOCurrently( weather )
    daily = FIODaily.FIODaily( weather )
    #for current location, pull daily weather data (store min and max for each day that location)
    #getting min and max weather for next 5 days 
    for day in range(2, 7):
        val = daily.get(day)
        if day == 2:
            min1 = val[ 'temperatureMin' ]
            max1 = val[ 'temperatureMax' ]
            if state_country in states:
                print(state_country)
        elif day ==3:
            min2 = val[ 'temperatureMin' ]
            max2 = val[ 'temperatureMax' ]
        elif day == 4:
            min3 = val[ 'temperatureMin' ]
            max3 = val[ 'temperatureMax' ]
        elif day == 5:
            min4 = val[ 'temperatureMin' ]
            max4 = val[ 'temperatureMax' ]
        elif day == 6:
            min5 = val[ 'temperatureMin' ]
            max5 = val[ 'temperatureMax' ]
    #create minAvg variable containing the city's average min temperature for the next 5 days, rounded to 2 decimal places
    minAvg = round((min1 + min2 + min3 + min4 + min5)/ 5 , 2)
    #create maxAvg variable containing the city's average max temperature for the next 5 days, rounded to 2 decimal places
    maxAvg = round((max1 + max2 + max3 + max4 + max5) / 5 ,2)
    
    # print variables for current iteration, one specific city - used as a way to test values of variables created
    # print(city, min1, max1, min2, max2, min3, max3, min4, max4, min5, max5, minAvg, maxAvg)
    
    # takes new variables created in current iteration of for loop and stores in newRow
    newRow = [city, min1, max1, min2, max2, min3, max3, min4, max4, min5, max5, minAvg, maxAvg]
    #add newRow to temp DataFrame
    temp.loc[len(temp)] = newRow
    

#print contents of temp DataFrame
#print(temp)
    
#write temp DataFrame to csv file (and remove indexes from csv output)
temp.to_csv('temp2.csv', index = False)


