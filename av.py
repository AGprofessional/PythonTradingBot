import pandas as pd
import requests
import io
from glom import glom
#this works
#https://www.alphavantage.co/documentation/#fx-intraday
#https://www.youtube.com/watch?v=d2kXmWzfS0w
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.techindicators import TechIndicators
import time

api_key = 'YVR9BGPFI9BA1KH9'
#forex
#fx = ForeignExchange(key=api_key, output_format='pandas')
#FXdata, FXmeta_data = fx.get_currency_exchange_intraday(from_symbol='EUR', to_symbol='USD',interval='1min', outputsize='full')


#crypto:
def getCrypto():
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD&interval=1min&outputsize=compact&apikey={}'.format(
    api_key)
    r = requests.get(url)
    Cjson = r.json()
    CtimeSeries = Cjson['Time Series Crypto (1min)']
#print(CtimeSeries)
#Cfirstkey=list(CtimeSeries.keys())[0]

#Cfirstval=list(CtimeSeries.values())[0]
#print(Cfirstkey, Cfirstval)
    Cnext=next(iter(CtimeSeries.items()))
   # print(type(Cnext))
    CnextValue = Cnext[1]
    getCrypto.open = CnextValue['1. open']
    print("---",getCrypto.open)
    high = CnextValue['2. high']
    low = CnextValue['3. low']
    close = CnextValue['4. close']
    volume = CnextValue['5. volume']
    #print("c next open-->", CnextOpen)


#stocks
def getStocks():
    stock = TimeSeries(key=api_key, output_format='pandas')
    Sdata, Smeta_data = stock.get_intraday(symbol='MRIN', interval='1min', outputsize='full')
    currCandle = Sdata.head(1)
    high = currCandle['2. high']
    low = currCandle['3. low']
    close = currCandle['4. close']
    open = currCandle['1. open']


def getData():
    #getCrypto()



    #tech indicators
    tech = TechIndicators(key=api_key, output_format='pandas')
    TdataEMA, Tmeta_dataEMA = tech.get_ema(symbol='MRIN', interval='1min', time_period='15', series_type='close')
    currEMA = TdataEMA.tail(1)
    #print(currEMA)
    TdataRSI, Tmeta_dataRSI = tech.get_rsi(symbol='MRIN', interval='1min', time_period='14', series_type='close')
    currRSI = TdataRSI.tail(1)
    #print(TdataRSI)
    #print(currRSI)
    TdataMACD, Tmeta_dataMACD = tech.get_macd(symbol='MRIN', interval='1min', series_type='close', fastperiod='12', slowperiod='26', signalperiod='9')
    currMACD = TdataMACD.head(1)
   # print(TdataMACD)
   # print(currMACD)




#getData()


#print(data)
#time.sleep(60)

#minute=3
#while (minute>0):
#   data, meta_data = ts.get_currency_exchange_intraday(from_symbol='EUR', to_symbol='USD',interval='1min', outputsize='compact')
#   most_recent=data.iloc[0]
#   print(most_recent)
#   time.sleep(60)
#   minute=minute-1

