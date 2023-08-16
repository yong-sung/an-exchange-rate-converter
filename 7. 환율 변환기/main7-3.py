import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter

cc = CurrencyConverter()
print(cc.convert(1, 'USD','KRW'))

# 사이트에서 링크주소 파일을 다운로드 받을 수 없어서 에러 발생. 사이트에서 더 이상 제공 X
def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    
    url = "https://kr.investing.com/currencies/{}-{}".format(target1, target2)
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find('span', {"data-test": "instrument-price-last"})
        
        if containers:
            exchange_rate = containers.text.strip()
            print(f"Exchange rate {target1}/{target2}: {exchange_rate}")
        else:
            print("Could not find exchange rate information on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Call the function with the desired currency pair
get_exchange_rate('usd', 'krw')
