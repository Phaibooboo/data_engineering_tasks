#task 3

#import requests library
import requests

#generate response
url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
data = response.json()


#Extract all male and female profiles into a different list
profiles = data['results']

males = []
females = []
others = []

for profile in profiles:
    if profile['gender'] == 'male':
        males.append(profile) 
    elif profile['gender'] == 'female':
        females.append(profile)
    else:
        others.append(profile)     
    
#Extract all dob date into a list.
dates = []

for profile in profiles:
    dates.append(profile['dob']['date'])

print(dates)

#Extract concatenated first name and last name into a list
full_names = []

for profile in profiles:
    full_names.append(profile['name']['first'] + " " + profile['name']['last'])

print(full_names)