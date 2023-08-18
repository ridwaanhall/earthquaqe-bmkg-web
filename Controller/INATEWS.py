import requests

class ReadUrl:
    def read_json(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

class INA_TEWS:
    def news(self):
        reader = ReadUrl()
        json_data = reader.read_json('https://earthquaqe-bmkg-api.ridwaanhall.repl.co/new.json')
        return json_data
