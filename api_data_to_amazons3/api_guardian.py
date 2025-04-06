import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://content.guardianapis.com/search?from-date=2025-01-01&to-date=2025-02-01&q=nigeria&api-key=b58bf858-d847-4ce6-a5b5-b729e08808a9'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print('check status code!!!')

articles_with_nigeria = data['response']['results']
article_titles = [articles["webTitle"] for articles in articles_with_nigeria]
df_article_titles = pd.DataFrame(article_titles)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
                        aws_secret_access_key=os.getenv('aws_secret_key'),
                        region_name=os.getenv('region'))

wr.s3.to_csv(
    df=df_article_titles,
    path="s3://wofais-aws-bucket/guardian_api/article_titles.csv",
    boto3_session=session,
    mode="append",
    dataset=True
   )
