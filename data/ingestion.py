## importing packages needed to run code
import pandas as pd ## install pandas for general file types
import requests ## import request for web requests
import json ## for json files
from google.cloud import bigquery ##importing bigquery files from google cloud

## section1
tab1 = pd.read_excel('data/dailyActivity.xls') ## import first tab of an excel file
tab2 = pd.read_excel('data/dailyActivity.xls', sheet_name= 1) ## import second table of an excel workbook|| you may also call the sheet name but calling its 'actual name'
tab1 ## display tab1
tab2 ## display tab2


## section 2
apiDataset = 'https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data'
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data') ## bring in open source json API and calling source apiDataset
data = apiDataset ## defining the variable data
data = data.json() ## run request as json
apiDataset = pd.read_json('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data') ## read json file
apiDataset ## display json file


## section 3
GOOGLE_APPLICATION_CREDENTIALS = 'brittany-507-d4f0dd46a096.json'
client = bigquery.Client.from_service_account_json('/Users/brittanykusi-gyabaah/Downloads/brittany-507-d4f0dd46a096.json') ## create bigquery client
## query public dataset
query_job = client.query('SELECT * FROM `bigquery-public-data.geo_us_census_places.places_new_york` LIMIT 100') ## query public dataset
## get results
results = query_job.result() ## get results of query
## putresults into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe()) ## put results into dataframe with the variable bigquery1
client = bigquery.Client.from_service_account_json('/Users/brittanykusi-gyabaah/Downloads//brittany-507-6906018882e5.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.genomics_cannabis.MNPR01_201703` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results of query
## putresults into dataframe
bigquery2 = pd.DataFrame(results.to_dataframe()) ## put results into dataframe with the variable bigquery1

