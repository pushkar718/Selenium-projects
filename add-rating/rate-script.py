import requests,string,random


for i in range(0,10):
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=8))
    headers = {
        'Host': 'testapi.referloan.in',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://qa.referloan.in/',
        'Content-Type': 'application/json',
        # 'Content-Length': '58',
        'Origin': 'https://qa.referloan.in',
        'Dnt': '1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        'Connection': 'close',
    }

    json_data = {
        # change bank-product_id [API] for changing the product
        'bank_product_id': 127,
        'rating': 5,
        'session_id': str(res),
    }

    response = requests.post('https://testapi.referloan.in/api/add-rating/', headers=headers, json=json_data)