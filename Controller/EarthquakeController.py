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
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json')
    return json_data

  def maps(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json')
    coordinates_str = json_data["info"]["point"]["coordinates"]
    headline = json_data['info']['headline']
    longitude, latitude = map(float, coordinates_str.split(','))
    return longitude, latitude, headline

  #def live30event(self):
  #    reader = ReadUrl()
  #    json_data = reader.read_json('https://earthquake-bmkg-api.ridwaanhall.repl.co/live30event.json')
  #    return json_data

  def live30event(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/live30event.json')
    gempa_list = json_data["Infogempa"]["gempa"]
    total_data = len(json_data["Infogempa"]["gempa"])
    dalam_values = [float(gempa["dalam"]) for gempa in gempa_list]
    mag_values = [float(gempa["mag"]) for gempa in gempa_list]
    average_dalam = sum(dalam_values) / len(
      dalam_values) if dalam_values else 0
    average_mag = sum(mag_values) / len(mag_values) if mag_values else 0
    return json_data, average_dalam, average_mag, total_data

  def last30event(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/last30event.json')
    info_list = json_data["alert"]["info"]
    magnitude_values = [float(info["magnitude"]) for info in info_list]
    depth_values = [float(info["depth"].split()[0]) for info in info_list
                    ]  # Extract the depth value and convert to float
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(info_list)
    return json_data, average_magnitude, average_depth, total_data

  def last30feltevent(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/last30feltevent.json')
    info_list = json_data["alert"]["info"]
    magnitude_values = [float(info["magnitude"]) for info in info_list]
    depth_values = [float(info["depth"].split()[0]) for info in info_list
                    ]  # Extract the depth value and convert to float
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(info_list)
    return json_data, average_magnitude, average_depth, total_data

  def last30tsunamievent(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/last30tsunamievent.json'
    )
    info_list = json_data["alert"]["info"]
    magnitude_values = [float(info["magnitude"]) for info in info_list]
    depth_values = [float(info["depth"].split()[0]) for info in info_list
                    ]  # Extract the depth value and convert to float
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(info_list)
    return json_data, average_magnitude, average_depth, total_data

  def EmgempaQL(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/EmgempaQL.json')
    features = json_data.get("features", [])
    magnitude_values = [
      float(feature["properties"]["mag"]) for feature in features
    ]
    depth_values = [
      float(feature["properties"]["depth"]) for feature in features
    ]
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(features)  # Calculate the total number of data entries
    return json_data, average_magnitude, average_depth, total_data

  def katalog_gempa(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/katalog_gempa.json')
    features = json_data.get("features", [])
    magnitude_values = [
      float(feature["properties"]["mag"]) for feature in features
    ]
    depth_values = [
      float(feature["properties"]["depth"]) for feature in features
    ]
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(features)  # Calculate the total number of data entries
    return json_data, average_magnitude, average_depth, total_data

  def histori(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/histori.json')
    features = json_data.get("features", [])
    magnitude_values = [
      float(feature["properties"]["mag"]) for feature in features
    ]
    depth_values = [
      float(feature["properties"]["depth"]) for feature in features
    ]
    average_magnitude = sum(magnitude_values) / len(
      magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(
      depth_values) if depth_values else 0
    total_data = len(features)  # Calculate the total number of data entries
    return json_data, average_magnitude, average_depth, total_data


class BMKG_Data:

  def maps(self):
    reader = ReadUrl()
    json_data = reader.read_json('https://earthquake-bmkg-api.ridwaanhall.repl.co/autogempa.json')
    gempa_data = json_data["Infogempa"]["gempa"]
    latitude, longitude = map(float, gempa_data["point"]["coordinates"].split(','))
    return latitude, longitude, gempa_data

  
  def news(self):
    reader = ReadUrl()
    json_data = reader.read_json(
      'https://earthquake-bmkg-api.ridwaanhall.repl.co/autogempa.json')
    return json_data

  def recentEQ(self):
    reader = ReadUrl()
    json_data = reader.read_json(
        'https://earthquake-bmkg-api.ridwaanhall.repl.co/gempaterkini.json')
    gempa_list = json_data["Infogempa"]["gempa"]
    magnitude_values = [float(gempa["Magnitude"]) for gempa in gempa_list]
    depth_values = [float(gempa["Kedalaman"].split()[0]) for gempa in gempa_list]
    average_magnitude = sum(magnitude_values) / len(magnitude_values) if magnitude_values else 0
    average_depth = sum(depth_values) / len(depth_values) if depth_values else 0
    total_data = len(gempa_list)  # Calculate the total number of data entries
    return json_data, average_magnitude, average_depth, total_data

# ================


