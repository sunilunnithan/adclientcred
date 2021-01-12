import requests, json
from decouple import config

token_url = "https://login.microsoftonline.com/8e04fb39-8906-4dd2-9cd2-b09d5ba3a8a4/oauth2/v2.0/token"
test_api_url = "https://graph.microsoft.com/v1.0/users"

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
scope = "https://graph.microsoft.com/.default"


data = "client_id=" + client_id + "&scope=" + scope + "&client_secret=" + client_secret + "&grant_type=client_credentials"

access_token_response = requests.post(
    token_url,
    data = data,
    verify=False,
    allow_redirects= False,
    auth = (client_id, client_secret)
)

print(access_token_response.headers)
print(access_token_response.text)