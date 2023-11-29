import requests
import os
import dotenv

WEATHER_API_ENDPOINT="https://api.openweathermap.org/data/2.5/weather"
LAT_LON_API_ENDPOINT="http://api.openweathermap.org/geo/1.0/direct"
def check_for_weather(lat:str,lon:str):
    dotenv.load_dotenv("./.env")
    params={
        "lat":lat,
        "lon":lon,
        "appid":os.getenv("appid")
    }
    response=requests.get(url=WEATHER_API_ENDPOINT,params=params)
    weather_id=response.json()["weather"][0]["id"]
    # print(response.text)
    if (weather_id<623):
        return [True,response.json()]
    else:
        return [False,response.json()]
    
def lat_lon(city:str,country_code="IN"):
    dotenv.load_dotenv("./.env")
    params={"q":f"{city},{country_code}",
            'limit':"1",
            "appid":os.getenv("appid")
        
    }
    respose=requests.get(url=LAT_LON_API_ENDPOINT,params=params)
    # print(respose.text)
    return (str(respose.json()[0]["lat"]),str(respose.json()[0]["lon"]))
    
def weathe_city(city:str,country="IN"):
    loc=lat_lon(city,country)
    return(check_for_weather(loc[0],loc[1]))
    
if __name__=="__main__":
    temp=weathe_city("Chennai")
    print(temp)