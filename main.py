#Import the required module
import requests

#Input the API key and the url of that API
API_KEY = input("Enter your API key: ")
url = input("Enter the url of the API: ")

#Making a request
city = input("Enter a city name: ")
request_url = f"{url}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

#Get the full data
if response.status_code == 200: #This specific value for the status code shows that a request has been processed correctly
    data = response.json()
    
    #Extract the desired information
    city_country = data["sys"]["country"]
    print(city, "is a city located in", city_country)
    weather_descrip = data["weather"][0]["description"]
    print("Weather Description:",weather_descrip)
    temperature = data["main"]["temp"]
    print("Currently, the temperature in", city, "is", round(temperature-273.15,2), "Celsius, with a minimum of",round(data["main"]["temp_min"]-273.15,2),"Celsius, and a maximum of",round(data["main"]["temp_max"]-273.15,2),"Celsius")
    wind_speed = data["wind"]["speed"]
    print("The wind speed is at about", round(wind_speed*3.6,2),"km/h")
    
    
#Display an error if the request was not executed successfully
else:
    print("An error occurred")
