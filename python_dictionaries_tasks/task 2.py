#task 2: Extract all the competition names into a separate list.

#import requests library

import requests

#generate response
url = "http://api.football-data.org/v4/competitions/"
response = requests.get(url)
data = response.json()


#Extract competition names
competitions = data['competitions']
competition_names = []

for competition in competitions:
    competition_names.append(competition['name'])
    
print(competition_names)
