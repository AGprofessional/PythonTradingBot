import requests
import time
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

#get once
url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=1min&outputsize=full&apikey=YVR9BGPFI9BA1KH9'
r = requests.get(url)
data = r.json()

print(data)
print('---------------------------------------')

#get for each additional minute, starting with the next minute
time.sleep(5)
#get for the next i minutes
minutes = 3
i=minutes
while (i>0):
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=1min&outputsize=compact&apikey=YVR9BGPFI9BA1KH9'
    r = requests.get(url)
    data = r.json()

    print(data[0])
    i=i-1
    time.sleep(5)
    print('---------------------------------------')
