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
      'https://08af913f-9472-4b1a-b6aa-625e70d2d226-00-1qo7jyrgk2g2p.global.replit.dev/new.json')
    return info_dashboard

  def maps_dashboard(self):
    reader = ReadData()
    json_data = reader.read_json(
      'https://08af913f-9472-4b1a-b6aa-625e70d2d226-00-1qo7jyrgk2g2p.global.replit.dev/new.json')
    coordinates_str = json_data["info"]["point"]["coordinates"]
    headline = json_data['info']['headline']
    longitude, latitude = map(float, coordinates_str.split(','))
    return longitude, latitude, headline

  def Naration(self):
    reader = ReadData()
    info_dashboard = reader.read_json(
      'https://08af913f-9472-4b1a-b6aa-625e70d2d226-00-1qo7jyrgk2g2p.global.replit.dev/new.json')
    eventid = info_dashboard['info']['eventid']
    url = f'https://bmkg-content-inatews.storage.googleapis.com/{eventid}_narasi.txt'
    response = requests.get(url)
    narasi_text = response.text
    return narasi_text


class DashboardStatistics:

  def McountList(self):
    # URL for the JSON data
    url = "https://08af913f-9472-4b1a-b6aa-625e70d2d226-00-1qo7jyrgk2g2p.global.replit.dev/last30feltevent.json"
  
    # Fetch JSON data from the URL
    response = requests.get(url)
    json_data = response.json()
  
    # Initialize a dictionary to store the count of magnitudes for each level category
    magnitude_counts = {
      'I': 0,
      'II-III': 0,
      'IV': 0,
      'V': 0,
      'VI': 0,
      'VII': 0,
      'VIII': 0,
      'IX-X': 0
    }
  
    # Loop through the info entries and categorize magnitudes by level
    for info in json_data['alert']['info']:
      magnitude = float(info['magnitude'])
  
      if magnitude <= 1.99999999:
        magnitude_counts['I'] += 1
      elif magnitude <= 3.99999999:
        magnitude_counts['II-III'] += 1
      elif magnitude <= 4.99999999:
        magnitude_counts['IV'] += 1
      elif magnitude <= 5.99999999:
        magnitude_counts['V'] += 1
      elif magnitude <= 6.99999999:
        magnitude_counts['VI'] += 1
      elif magnitude <= 7.99999999:
        magnitude_counts['VII'] += 1
      elif magnitude <= 8.99999999:
        magnitude_counts['VIII'] += 1
      else:
        magnitude_counts['IX-X'] += 1
  
    # Convert the dictionary values to a list
    mag30felt = [
      magnitude_counts[level] for level in magnitude_counts
    ]
    return mag30felt

  def magHistory(self):
    # URL for the JSON data
    url = "https://08af913f-9472-4b1a-b6aa-625e70d2d226-00-1qo7jyrgk2g2p.global.replit.dev/histori.json"
  
    # Fetch JSON data from the URL
    response = requests.get(url)
    json_data = response.json()
  
    # Initialize a dictionary to store the count of magnitudes for each level category
    magnitude_counts = {
      'I': 0,
      'II-III': 0,
      'IV': 0,
      'V': 0,
      'VI': 0,
      'VII': 0,
      'VIII': 0,
      'IX-X': 0
    }

    for feature in json_data['features']:
      properties = feature['properties']
      magnitude = float(properties['mag'])
    # Loop through the info entries and categorize magnitudes by level
    #for properties in json_data['features']['properties']:
      #magnitude = float(properties['mag'])
  
      if magnitude <= 1.99999999:
        magnitude_counts['I'] += 1
      elif magnitude <= 3.99999999:
        magnitude_counts['II-III'] += 1
      elif magnitude <= 4.99999999:
        magnitude_counts['IV'] += 1
      elif magnitude <= 5.99999999:
        magnitude_counts['V'] += 1
      elif magnitude <= 6.99999999:
        magnitude_counts['VI'] += 1
      elif magnitude <= 7.99999999:
        magnitude_counts['VII'] += 1
      elif magnitude <= 8.99999999:
        magnitude_counts['VIII'] += 1
      else:
        magnitude_counts['IX-X'] += 1
  
    # Convert the dictionary values to a list
    magHistoryList = [
      magnitude_counts[level] for level in magnitude_counts
    ]
    return magHistoryList

