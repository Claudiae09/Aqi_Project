import main_functions
import requests
import folium


# "Task 6"
#Created a function to read API key from api_key.json
def get_api_key(filename):
    all_keys = main_functions.read_from_file("api_key.json") #Read the contents of the JSON file
    return all_keys["aqi_api_key"] #Returned the API key from the data

my_aqi_api_key = get_api_key("aqi_key.json") #
print(my_aqi_api_key)

"Task 7"
def get_aqi_data(api_key):
    url = "http://api.airvisual.com/v2/nearest_city?key="
    url_aqi = url + api_key
    #response = requests.get(url_aqi).json()
    #main_functions.save_to_file(response, "aqi.json")

get_aqi_data(my_aqi_api_key)

"Task 8"
def generate_map(data_filename,zoom_start):
    aqi_data = main_functions.read_from_file(data_filename)
    lat = aqi_data["data"]["location"]["coordinates"][1]
    long = aqi_data["data"]["location"]["coordinates"][0]
    m = folium.Map(location=[lat, long], zoom_start=zoom_start)
    folium.Marker(
        location=[lat, long],
        popup='AQI Station',
        icon=folium.Icon()
    ).add_to(m)
    m.save("map.html")

generate_map("aqi.json", 10)

"Task 9"
def display_aqi_info(data_filename):
    aqi_data = main_functions.read_from_file(data_filename)
    tempC = aqi_data["data"]["current"]["weather"]["tp"]
    tempF = (tempC * 9/5) + 32
    humid = aqi_data["data"]["current"]["weather"]["hu"]
    aqius = aqi_data["data"]["current"]["pollution"]["aqius"]

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

    print(
        f"The temperature is {tempC}ºC or {tempF:.1f}ºF, the humidity is {humid}%, and the index shows that the air quality is {air_quality}.")

display_aqi_info("aqi.json")