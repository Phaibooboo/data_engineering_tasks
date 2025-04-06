import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"
response = requests.get(url)

if response.status_code == 200:
    response = response.json()
else:
    print('check status code!!!')

joblist = response['jobs']
seniorlist = []
managerlist = []

for jobs in joblist:
    if 'Senior' in jobs['jobTitle']:
        seniorlist.append(jobs['jobTitle'])
    if 'Manager' in jobs['jobTitle']:
        managerlist.append(jobs['jobTitle'])

df_seniorlist = pd.DataFrame(seniorlist)
df_managerlist = pd.DataFrame(managerlist)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
                        aws_secret_access_key=os.getenv('aws_secret_key'),
                        region_name=os.getenv('region'))
wr.s3.to_csv(
    df=df_seniorlist,
    path="s3://wofais-aws-bucket/jobtitles/seniorlist.csv",
    boto3_session=session,
    mode="append",
    dataset=True
   )

wr.s3.to_csv(
    df=df_managerlist,
    path="s3://wofais-aws-bucket/jobtitles/managerlist.csv",
    boto3_session=session,
    mode="append",
    dataset=True
   )
