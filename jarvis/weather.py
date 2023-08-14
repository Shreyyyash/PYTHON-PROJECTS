import requests,json
apikey="7040ea904442a45d6950ba584410ce59"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="
cityName = "kolhapur"
completeURL = baseURL + cityName + "&appid=" + apikey
response = requests.get(completeURL)
data = response.json()
# print(data)
print ("Current Temperature ", data["main"]["temp"]) 
print ("Current Temperature Feels like ", data["main"]["feels_like"]) 
print ("Current Temperature ",data["main"]["temp_max"])
print ("Current Temperature ", data["main"]["temp_min"])