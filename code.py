import ctypes 
import requests as req
import json
import time
import random
from os import listdir
from os.path import isfile, join

strings = ["Thunderstorm",'Drizzle', 'Rain', 'Snow', 'Mist', 'Haze', 'Fog', 'Squall', "Clear", "Clouds"]

url = "https://api.openweathermap.org/data/2.5/onecall?lat=48.2082&lon=16.3738&appid=a1d0a370f4b03bcb60190215d3dc31dd"

while True:
    resp = req.get(url)   
    
    forecast = json.loads(resp.text)
    
    loc = forecast["timezone"]
    temp = forecast["hourly"][2]["feels_like"] - 273.15
    cond = forecast["hourly"][2]["weather"][0]["main"]
    
    print(loc,temp,cond)
    
    path0 = "C:\\Users\\yurke\\Documents\\My_Projects\\Background\\dataset\\bing\\" + cond + " jpg computer background\\"
    
    onlyfiles = [f for f in listdir(path0) if isfile(join(path0, f))]
    
    r = random.randint(0,len(onlyfiles)-1)
    
    path = "C:\\Users\\yurke\\Documents\\My_Projects\\Background\\dataset\\bing\\" + cond + " jpg computer background\\" + onlyfiles[r]
    
    print(path)
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    
    time.sleep(6*1/10)