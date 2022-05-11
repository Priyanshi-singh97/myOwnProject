from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'path/to/file.json')

project_id = 'my-bq'
client = bigquery.Client(credentials= credentials,project=project_id)
