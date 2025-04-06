import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://randomuser.me/api/?results=500"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print('check status code!!!')

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

full_names = []
for profile in profiles:
    full_names.append(profile['name']['first'] + " " + profile['name']['last'])

df_full_names = pd.DataFrame(full_names)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
                        aws_secret_access_key=os.getenv('aws_secret_key'),
                        region_name=os.getenv('region'))

wr.s3.to_csv(
    df=df_full_names,
    path="s3://wofais-aws-bucket/random_user/full_names.csv",
    boto3_session=session,
    mode="append",
    dataset=True
   )
