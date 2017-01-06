import requests, json

api = "85ced2e33abffe6d1e901d2dff9a3"
url = "http://api.worldweatheronline.com/free/v2/weather.ashx?q=Porvoo&format=json&key="+api
req =requests.get(url=url,
                headers = {'Content-type':'application/json'})
loadedJSON = json.loads(req.text)

currentTemp = loadedJSON['data']['current_condition'][0]["temp_C"]
currentTime = loadedJSON['data']['current_condition'][0]["observation_time"]
currentDate = loadedJSON['data']['weather'][0]["date"]
currentCity = loadedJSON['data']['request'][0]["query"]
string_to_print = currentTemp + "," + currentTime + " " + currentDate+ "," + currentCity+"\n"

def _print_to_file(str):
    dataFile = open("tempData.dat", "a")
    dataFile.write(str)
    dataFile.close()
    return
print (currentTemp + " C",currentTime, currentDate, currentCity)
_print_to_file(string_to_print)
