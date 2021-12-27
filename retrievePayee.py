import requests
import json
import math

def retriveAllPayee(baseUrl,headers):#获取全部的payees到字典
  url = "{}/payees?perPage&page&term".format(baseUrl)
  payload = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  totalPage = math.ceil(response.json()['data']['meta']['total'] / 10)  # 得到页数
  payList = {}
  for i in range(1, totalPage + 1):  # 循环获取全部的payees
    urlSinglePage = "{}/payees?perPage&page={}&term".format(baseUrl, str(i))
    responseSinglePage = requests.request("GET", urlSinglePage, headers=headers, data=payload)
    allPayees = responseSinglePage.json()['data']['payees']
    for payee in allPayees:
      payList[payee['name']] = payee['payeeId']
  return payList

def createNewPayee(baseUrl,headers,name):#创建新的payee

  url = "{}/payees".format(baseUrl)

  payload = json.dumps({
    "payees": [
      {
        "name": name,
        "nickName": "",
        "company": "",
        "email": "",
        "phone": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "",
        "zip": "",
        "country": ""
      }
    ]
  })
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.json()['data']['payees'][0]['payeeId']

