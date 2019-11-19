import requests
import json
import csv

with open('mobileno.csv','r') as m:
    read=csv.reader(m)
    fields=
    
URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, '7A93ZTCNF4DJBFRY5OZU858PB0WK9MZT', 'UB2EHWA6F0QG3BC3', 'stage', '7088370902', 'nikita', 'Automated message!')
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)
