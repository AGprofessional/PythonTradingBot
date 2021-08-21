
import pandas as pd
import time

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
    getCrypto.high = CnextValue['2. high']
    getCrypto.low = CnextValue['3. low']
    getCrypto.close = CnextValue['4. close']
    getCrypto.volume = CnextValue['5. volume']
    #print("c next open-->", CnextOpen)
#getCrypto()

#stocks
def getStocks():
    #stock = TimeSeries(key=api_key, output_format='pandas')
    #Sdata, Smeta_data = stock.get_intraday(symbol='MRIN', interval='1min', outputsize='full')
    #currCandle = Sdata.head(1)
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MRIN&interval=1min&apikey={}'.format(api_key)
    r = requests.get(url)
    Sjson = r.json()
    StimeSeries = Sjson['Time Series (1min)']
    Snext = next(iter(StimeSeries.items()))
    # print(type(Cnext))
    SnextValue = Snext[1]
    getStocks.open = SnextValue['1. open']
    print("-stocks open--", getStocks.open)
    getStocks.high = SnextValue['2. high']
    getStocks.low = SnextValue['3. low']
    getStocks.close = SnextValue['4. close']
    getStocks.volume = SnextValue['5. volume']



    # getStocks.high = currCandle['2. high']
    # #print(getStocks.high)
    # getStocks.low = currCandle['3. low']
    # getStocks.close = currCandle['4. close']
    # getStocks.open = currCandle['1. open']
    # getStocks.volume = currCandle['5. volume']
#getStocks()

def getTechPandas():
    #tech indicators
    tech = TechIndicators(key=api_key, output_format='pandas')
    TdataEMA, Tmeta_dataEMA = tech.get_ema(symbol='MRIN', interval='1min', time_period='15', series_type='close')
    getTechPandas.currEMA = TdataEMA.tail(1)
    #print(currEMA)
    TdataRSI, Tmeta_dataRSI = tech.get_rsi(symbol='MRIN', interval='1min', time_period='14', series_type='close')
    getTechPandas.currRSI = TdataRSI.tail(1)
    #print(TdataRSI)
    #print(currRSI)
    TdataMACD, Tmeta_dataMACD = tech.get_macd(symbol='MRIN', interval='1min', series_type='close', fastperiod='12', slowperiod='26', signalperiod='9')
    getTechPandas.currMACD = TdataMACD.head(1)
   # print(TdataMACD)
   # print(currMACD)

def getTechJson():
    #ema
    url = 'https://www.alphavantage.co/query?function=EMA&symbol=MRIN&interval=1min&time_period=15&series_type=close&apikey={}'.format(api_key)
    e = requests.get(url)
    Tjson = e.json()
    Tset = Tjson['Technical Analysis: EMA']
    Tnext = next(iter(Tset.items()))
    TnextValue = Tnext[1]
    getTechJson.ema = TnextValue['EMA']
    print("-tech ema--", getTechJson.ema)

    #rsi
    url = 'https://www.alphavantage.co/query?function=RSI&symbol=MRIN&interval=1min&time_period=14&series_type=close&apikey={}'.format(api_key)
    r = requests.get(url)
    RSIjson = r.json()
    RSIset = RSIjson['Technical Analysis: RSI']

    RSInext = next(iter(RSIset.items()))

    RSInextValue = RSInext[1]
    getTechJson.rsi = RSInextValue['RSI']
    print("-tech rsi--", getTechJson.rsi)

    #macd
    url = 'https://www.alphavantage.co/query?function=MACD&symbol=MRIN&interval=1min&series_type=close&fastperiod=12&slowperiod=26&signalperiod=9&apikey={}'.format(api_key)
    m= requests.get(url)
    Mjson = m.json()
    Mset = Mjson['Technical Analysis: MACD']
    Mnext = next(iter(Mset.items()))
    MnextValue = Mnext[1]
    getTechJson.macd = MnextValue['MACD']
    print("-tech macd--", getTechJson.macd)
#getTechJson()


##algo for 1m chart
#getStocks()

#currEMA = av.currEMA
#high=av.high
#low = av.low
#currCandle=av.currCandle

#rule 1:
#high of candle must be greater than ema for two candles in a row
#then enter
#if order, then sell, store orders in hashmap

#i will monitor bot, and supply resistance and support levels

def placeOrder(resistance=0, support=0, takeProfit=2, stopLoss=0.5, tradeAmt=100):
    minute=0
    sellCount=0
    buyCount=0
    sellRuleCount=0
    buyRuleCount=0

    while (minute<500):
        #start timer immediately
    #get most recent data for current minute
        getStocks()
        getTechJson()
        # open = float(getCrypto.open)
        # #print(open)
        # low = float(getCrypto.low)
        #
        # close=float(getCrypto.close)
        # high=float(getCrypto.high)
        # volume=float(getCrypto.volume)
        open = float(getStocks.open)
        # #print(open)
        low = float(getStocks.low)

        close=float(getStocks.close)
        high=float(getStocks.high)
        volume=float(getStocks.volume)
        ema= float(getTechJson.ema)
        rsi=float(getTechJson.rsi)
    #diffx2 rule and ema----------------------
        #buy------------
        diff4Buy = low-ema
        diff4Sell = ema-low
        if (diff4Buy>0):
            buyCount+=1
            sellCount=0
        else:
            buyCount=0
            sellCount+=1

        #sell-----------
        if (diff4Sell>0):
            sellCount+=1
            buyCount=0
        else:
            sellCount=0
            buyCount+=1

        if (buyCount==2):
            buyRuleCount+=1
        if (sellCount==2):
            sellRuleCount+=1

    ##rsi rule-------------------------------------
        #get rsi
        if (rsi>=30 and rsi<=70):
            buyRuleCount+=1
        else:
            if (rsi>70 or rsi<30):
                sellRuleCount+=1

    ##get macd--do with talib later to get macd crossover-will need to look at a consistent SET of at least 15 minutes back to know if it's a sell or buy signal
    ##calculate resistance/support using statistics
    ##calculate probablity of sucessful trades with ML

    #place order-----------------------
        if (sellRuleCount==2):
            #place market sell order
            print("sold at: ", close)
        #get sell price
        #store it in hashtable
        if (buyRuleCount==2):
            #place market buy order
            print("bought at: ", open)

        #get buy price

        #store it in hashtable, after sell price is put, calculate %profit and store that in hashtable too
        buyPrice=0
        sellToTakeProfit = (1 + takeProfit / 100) * buyPrice
        sellToStopLoss = (1-stopLoss/100)*buyPrice
    #--take profit, stop loss, hard sell---------
        if (high>=sellToTakeProfit):
            #execute market sell order
            print("sold at: ", close)
        if (low<=sellToStopLoss):
            #execute market sell order
            print("sold at: ", close)


    #--------------------------------------------------------------------------
    #wait 60seconds before refreshing the data, change to async await later and wait while running algo, so it's exactly 60 second wait time
        time.sleep(60)
        minute += 1

placeOrder()