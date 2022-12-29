import requests,string,random


for i in range(2):
    headers = {
        # Change testapi -> api for going on master
        'Host':'testapi.referloan.in',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept':'application/json, text/plain, */*',
        'Accept-Language':'en-US,en;q=0.5',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'https://cms.referloan.in/admin/login',
        'Content-Type':'application/json',
        'Origin':'https://cms.referloan.in/admin/login',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        'Te':'trailers',
        'Connection':'close'
    }

    json_data = {"phone_no":'9667484050',
                 "full_name":"Mr ROBOT",
                 "bank_product_id":27}
    # Change testapi -> api for going on master
    response = requests.post('https://testapi.referloan.in/api/generate-otp', headers=headers, json=json_data)
    # print(response.text)