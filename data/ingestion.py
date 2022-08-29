## section 1
import pandas as pd ## install pandas for general file types
import requests ## import request for web requests
import json ## for json files
tab1 = pd.read_excel('data/dailyActivity.xls') ## import first tab of an excel file
tab2 = pd.read_excel('data/dailyActivity.xls', sheet_name= 1) ## import second table of an excel workbook|| you may also call the sheet name but calling its 'actual name'
tab1 ## display tab1
tab2 ## display tab2


## section 2
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data') ## bring in open source json API and calling source apiDataset
data = apiDataset ## defining data
data = data.json() ## run request as json
apiDataset = pd.read_json('https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data') ## read json file
apiDataset ## display json file


## section 3
### BIGQUERY
## first need to load api key that you created based on readme instructions
# connect to bigquery, be sure to update the name of your file, this is currently mine
client = bigquery.Client.from_service_account_json('ingestion/example_files/bigquery/hants-507-0569c50b5a7c.json') ## create bigquery client
## query public dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query public dataset
## get results
results = query_job.result() ## get results
## putresults into dataframe
df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe
