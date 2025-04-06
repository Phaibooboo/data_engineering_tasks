import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = "http://api.football-data.org/v4/competitions/"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print('check status code!!!')

competitions = data['competitions']
competition_names = []

for competition in competitions:
    competition_names.append(competition['name'])

df_competition_names = pd.DataFrame(competition_names)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
                        aws_secret_access_key=os.getenv('aws_secret_key'),
                        region_name=os.getenv('region'))

wr.s3.to_csv(
    df=df_competition_names,
    path="s3://wofais-aws-bucket/competition/list_of_competitions.csv",
    boto3_session=session,
    mode="append",
    dataset=True
   )
