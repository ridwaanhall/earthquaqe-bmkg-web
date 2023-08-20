import requests


class ReadData:

  def read_json(self, url):
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    return None


class Dashboard:
  def news_dashboard(self):
    reader = ReadData()
    info_dashboard = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json')
    return info_dashboard

  def maps_dashboard(self):
    reader = ReadData()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json')
    coordinates_str = json_data["info"]["point"]["coordinates"]
    headline = json_data['info']['headline']
    longitude, latitude = map(float, coordinates_str.split(','))
    return longitude, latitude, headline
