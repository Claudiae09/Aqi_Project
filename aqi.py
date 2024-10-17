import main_functions
import requests
import folium


# "Task 6"
#Created a function to read API key from api_key.json
def get_api_key(filename):
    all_keys = main_functions.read_from_file("api_key.json") #Read the contents of the JSON file
    return all_keys["aqi_api_key"] #Returned the API key from the data

my_aqi_api_key = get_api_key("aqi_key.json") #assigning a varible to the function that gets the api key from file
print("This is my API key: " + my_aqi_api_key) #prints out the api key

#"Task 7"
# Function that gets AQI data from the API
def get_aqi_data(api_key):
    url = "http://api.airvisual.com/v2/nearest_city?key=" #URL that is used to make the API request
    url_aqi = url + api_key # Concatinating both URL and API to make full request
    #response = requests.get(url_aqi).json() #Make a GET request and parse the response as JSON
    #main_functions.save_to_file(response, "aqi.json") #Save the data to a file named aqi.json

get_aqi_data(my_aqi_api_key) #function that gets the data using the API key

#"Task 8"
# Function that generates a map using the AQI data
def generate_map(data_filename,zoom_start):
    aqi_data = main_functions.read_from_file(data_filename) # Read Aqi data from the specified file name
    lat = aqi_data["data"]["location"]["coordinates"][1] #extract latitude from the coordinates in data
    long = aqi_data["data"]["location"]["coordinates"][0] #extract longitude from the coordinates in data
    m = folium.Map(location=[lat, long], zoom_start=zoom_start) #creates a folium map based on the coordinates and zoom level
    folium.Marker(
        location=[lat, long],
        popup='AQI Station',
        icon=folium.Icon()
    ).add_to(m)
    m.save("map.html") #saved map to html file

generate_map("aqi.json", 10) #called function to generate map using aqi data from json file

#"Task 9"
# Function to display aqi info
def display_aqi_info(data_filename):
    aqi_data = main_functions.read_from_file(data_filename) #read data from the json file
    tempC = aqi_data["data"]["current"]["weather"]["tp"] #gets the celcius temperature
    tempF = (tempC * 9/5) + 32 #calculates the Fahrenheit temperature using celcius
    humid = aqi_data["data"]["current"]["weather"]["hu"] #gets the humidity from json file
    aqius = aqi_data["data"]["current"]["pollution"]["aqius"] #gets the aqi value from the json file

#Determines air quality based on AQI value
    if aqius <= 50:
        air_quality = "good"
    elif aqius <= 100:
        air_quality = "moderate"
    elif aqius <= 150:
        air_quality = "unhealthy for sensitive groups"
    elif aqius <= 200:
        air_quality = "unhealthy"
    elif aqius <= 300:
        air_quality = "very unhealthy"
    else:
        air_quality = "hazardous"  # Optionally handle values above 300

#Prints what the temperature and how humid it is as well as the air quality
    print(
        f"The temperature is {tempC}ºC or {tempF:.1f}ºF, the humidity is {humid}%, and the index shows that the air quality is {air_quality}.")

#Calls function that displays AQI information using data from the aqi.json
display_aqi_info("aqi.json")