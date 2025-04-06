#task 1: Extract all senior roles and manager roles into a different list.

#import requests library

import requests

#generate response
url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"
response = requests.get(url)
response = response.json()

#Extract all senior roles and manager roles
joblist = response['jobs']
seniorlist = []
managerlist = []

for jobs in joblist:
    if 'Senior' in jobs['jobTitle']:
        seniorlist.append(jobs['jobTitle']) 
    if 'Manager' in jobs['jobTitle']:
        managerlist.append(jobs['jobTitle'])
    
print(seniorlist)
print(managerlist)