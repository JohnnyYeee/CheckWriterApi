import requests
import json
#获取bankaccountid
baseUrl = 'https://test.onlinecheckwriter.com/api/v3'
AUTH_TOKEN = 'nupZMp3dD5uTwvlVmPtmeMtEVwJzAvuVTKs9AHFoAdVSl3ngpEMCmlxZPzR2'
url = "{}/bankAccounts?perPage&page&term".format(baseUrl)

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer {} '.format(AUTH_TOKEN),
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

