import requests
import json


def createCheck(baseUrl,headers,amount,bankAccountId,payeeId,cateId):
  url = "{}/checks".format(baseUrl)
  payload = json.dumps({
    "checks": [
      {
        "bankAccountId": bankAccountId,
        "payeeId": payeeId,
        "categoryId": cateId,
        "serialNumber": None,
        "issueDate": None,
        "amount": amount,
        "memo": "second, Test check using API",
        "note": "",
        "accountNumber": "458756",
        "invoiceNumber": "2545",
        "noSign": 0,
        "noAmount": 0,
        "noDate": 0,
        "noPayee": 0,
        "voucherId": None
      }
    ]
  })


  response = requests.request("POST", url, headers=headers, data=payload)

  #print(response.text)