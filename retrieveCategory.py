import requests
import json
import math

def retriveAllCate(baseUrl,headers):#获取全部的category到字典
    url = "{}/categories".format(baseUrl)
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.json())
    totalPage = math.ceil(response.json()['data']['meta']['total'] / 10)  # 得到页数
    cateList = {}
    for i in range(1, totalPage + 1):  # 循环获取全部的category
        urlSinglePage = "{}/categories?page={}&perPage&term".format(baseUrl, str(i))
        responseSinglePage = requests.request("GET", urlSinglePage, headers=headers, data=payload)
        allCate = responseSinglePage.json()['data']['categories']
        for cate in allCate:
            cateList[cate['name']] = cate['categoryId'] #只需要计算name，一旦创建type不能更改
    #print(len(cateList))
    return cateList

def createNewCate(baseUrl,headers,cateName,catetype='expense'):#创建新的category，type只能选择expense or income
    url = "{}/categories?page&perPage&term".format(baseUrl)
    payload = json.dumps({
        "name": cateName,
        "type": catetype
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.json())
    #print(response.json()['data']['categoryId'])
    return response.json()['data']['categoryId']

