from datetime import datetime, timedelta
import requests

class WeatherAPI :
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        self.session = requests.Session()

        self.default_parames = {
            'appid' : api_key,
            'units' : 'metric',
            'lang' : 'kr'
        }

    def _make_request(self, endpoint, params=None) :
        if params is None :
            params = {}

        request_params = self.default_parames.copy()
        request_params.update(params)

        response = self.session.get(f"{self.base_url}/{endpoint}",
                                    params=request_params)
        
        return response

    def get_current_temp(self, city, country_code=None) :
        if country_code :
            q = f"{city},{country_code}"
        else : 
            q = city

        data = self._make_request('weather', {'q' : q})
        data = data.json()

        return data['main']['temp']
    

api_key = '#'
weather_api = WeatherAPI(api_key)
print(f"현재 서울의 온도 : ", weather_api.get_current_temp('Seoul', 'KR'))
