import requests
#import getBankAccountId
import retrievePayee
import retrieveCategory
import check
import xlrd

if __name__ == '__main__':
    #import data from excel
    file = 'data.xls'
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    #print(data.sheet_loaded(0)) #check load successful
    nameList = table.col_values(0, start_rowx=1, end_rowx=None)
    amountList = table.col_values(1, start_rowx=1, end_rowx=None)
    cataListExcel = table.col_values(2, start_rowx=1, end_rowx=None)
    #################
    baseUrl = 'https://test.onlinecheckwriter.com/api/v3'
    token = 'Enter your Token here'####Enter your Token here
    bankAccountId = 'Q36gYVewyz3o4dx7bDn'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {} '.format(token),
        'Accept': 'application/json'
    }
    payeeList = retrievePayee.retriveAllPayee(baseUrl, headers)
    cataList = retrieveCategory.retriveAllCate(baseUrl, headers)
    n = len(nameList)
    cateType = 'expense'
    for i in range(n):
        payeeName = nameList[i]
        cateName = cataListExcel[i]
        amount = amountList[i]
        if payeeName in payeeList.keys():
            payeeId = payeeList[payeeName]
        else:
            payeeId = retrievePayee.createNewPayee(baseUrl, headers, payeeName)
            payeeList[payeeName] = payeeId

        # cataList = retrieveCategory.retriveAllCate(baseUrl,headers)
        if cateName in cataList.keys():
            cateId = cataList[cateName]
        else:
            cateId = retrieveCategory.createNewCate(baseUrl, headers, cateName, cateType)
            payeeList[cateName] = cateId

        check.createCheck(baseUrl, headers, amount, bankAccountId, payeeId, cateId)



