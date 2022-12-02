from django.shortcuts import render
from patterns import patterns
import yfinance as yf
import nsepython
import talib
from django.http import HttpResponse
import os
import pandas as pd
import csv
from tvDatafeed import TvDatafeed,Interval
import test_pattern
from test_pattern import pattern
import matplotlib
import mplfinance as mpf
from yahoo_fin.stock_info import *
# Create your views here.
tv=TvDatafeed()
def home(request):
    get_patterns=request.GET.get('patterns',None)
    stocks={}
    with open('dataset2/companies.csv',encoding="utf-8") as f:
            for row in csv.reader(f):
                stocks[row[0]]={'company':row[1]}
    if get_patterns:
        
        datafiles=os.listdir('dataset2/daily')
        for filename in datafiles:
            df=pd.read_csv('dataset2/daily/{}'.format(filename))
            pattern_function=getattr(talib,get_patterns)
            symbol=filename.split(".csv")[0]
            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                #print(results)
              
                last = results.tail(1).values[0]
                #print(last)
                if last>0:
                    stocks[symbol][get_patterns] = 'bullish'
                    print("bullish")
                elif last<0:
                    stocks[symbol][get_patterns] = 'bearish'
                    print("bearish")
                else:
                    stocks[symbol][get_patterns] = 'None'
                    
                    

                
            except Exception as e:
                pass

    return render(request,'newindex.html',{'patterns':patterns,'stocks':stocks,'get_patterns':get_patterns})































def index(request):
    pattern1=request.GET.get('patterns',None)
    #print(pattern1)
    stocks={}
    with open('dataset2/companies.csv',newline=",",encoding="utf_8") as f:
        for row in csv.reader(f):
            stocks[row[0]]={'company':row[0]}
           
    if pattern1:
        print(pattern1)
        datafiles=os.listdir('dataset2/daily')
        #print(datafiles)
        for filename in datafiles:
            df=pd.read_csv('dataset2/daily/{}'.format(filename))
            #print(df)
            pattern_function=getattr(talib,pattern1)
            #symbol1=filename.split(".")[0]
            symbol=filename.split(".csv")[0]
            print(symbol)
            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                print(results)
                last = results.tail(1).values[1]
                #print(last)

                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None


            except Exception as e:
                 print('failed on filename: ', filename)
    return render(request,'index.html',{'patterns':patterns,'stocks':stocks,'pattern1':pattern1})

def snapshot(request):

    #with open ('dataset/ind_nifty50list.csv') as f:
       # companies=f.read().splitlines()
        #count=0
        stock_picker=tickers_nifty50()
        print(stock_picker)
        companies=["SBIN.NS","AXISBANK.NS","ICICIBANK.NS","RELIANCE.NS"]
        for company in stock_picker:
            #symbol=company.split(',')[0]
            print(company)
            
            df=yf.download(company,start="2019-01-01",end="2022-11-11")
            print(df)
            df.to_csv('dataset2/daily/{}.csv'.format(company))
            
        return render(request,'index.html')


def test(request):
    price_data=tv.get_hist('INFY','NSE',Interval.in_15_minute,n_bars=500)
    #print(price_data)
    close_price=price_data.close
    #print(close_price)
    #print(talib.get_function_groups().keys())
    sma=talib.SMA(close_price,timeperiod=21)
    addplot=mpf.make_addplot(sma)
    a=mpf.plot(price_data,addplot=addplot,type='candle',style='yahoo')


    return render(request,'test.html',{'pattern':pattern,'a':a})



def newindex(request):
    get_patterns=request.GET.get('patterns',None)
    stocks={}

    if get_patterns:
        print('trupti')
        datafiles=os.listdir('dataset2/daily')
        for filename in datafiles:
            df=pd.read_csv('dataset2/daily/{}'.format(filename))
            #print(df)
            pattern_function=getattr(talib,get_patterns)
            #symbol1=filename.split(".")[0]
            symbol=filename.split(".csv")[0]
            print(symbol)
            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                #print(results)
                #print(type(results))
                last = results.tail(1).values[0]
                #print(last)
                #print(type(last))
                #if int(last)>0:
                #    stocks[symbol][get_patterns] = 'bullish'
                #    #pattern='bullish'
                #    #print(stocks[symbol][get_patterns])
                #elif int(last)<0:
                #    stocks[symbol][get_patterns] = 'bearish'
                #    #pattern='bearish'
                #    #print(stocks[symbol][get_patterns])
                #else:
                #    stocks[symbol][get_patterns] = None
                    #pattern="None"
                    #print(stocks[symbol][get_patterns])
                
            except Exception as e:
                print('failed on filename: ', filename)

 
    return render(request,'newindex.html',{'patterns':patterns,'get_patterns':get_patterns,'stocks':stocks.keys})





#with open('dataset/companies1.csv') as f:
    #    csvreader = csv.reader(f)
    #    for row in csv.reader(f):
    #       stocks[row[0]]={'company':row[1]}
    #       print(stocks)


#    if pattern1:
#       datafiles=os.listdir('dataset/daily')
#      print(datafiles)
#       for filename in datafiles:
#        df=pd.read_csv('dataset/daily/{}'.format(filename))
#        pattern_function=getattr(talib,'pattern1')
#        symbol1=filename.split('.')[0]
#        symbol2=filename.split('.')[1]
#        symbol=symbol1+"."+symbol2
#        #print(symbol)
#        #symbol=["AXISBANK.NS","ICICIBANK.NS","RELIANCE.NS","SBIN.NS"]
#        result=pattern_function(df['Open'],df['High'],df['Low'],df['Close'])
#        #print(type(result))
#        last=result.tail(7).values[0]
#        #print(type(last))
#        #if last > 0:
#        #    stocks[symbol][pattern1]='bullish'
#        #    
#        #elif last<0:
#        #    stocks[symbol][pattern1]='bearish'
#        #else:
#        #    stocks[symbol][pattern1]=None
#        #    print("{} triggered {}".format(filename,pattern1))'''

#for stock,i in stocks.items():
    #    print(stock)
    #    print(i)

#    stocks={}
#         with open
#            
#                
                       #value23=stocks.values
            #print(stocks.keys)
 #           data=pd.DataFrame.from_dict({(i,j): stocks[i][j] for i in stocks.keys() for j in stocks[i].keys()},orient='index')
 #           #print(data.iloc[:, 0])
##
 #           data1=data.iloc[:, 0].str.split(',', expand=True)
##
            #from csv import writer
 #
            ## List that we want to add as a new row
            #List = [str(symbol),pattern ]
            #
            ## Open our existing CSV file in append mode
            ## Create a file object for this file
            #with open('event.csv', 'a') as f_object:
            #
            #    # Pass this file object to csv.writer()
            #    # and get a writer object
            #    writer_object = writer(f_object)
            #
            #    # Pass the list as an argument into
            #    # the writerow()
            #    writer_object.writerow(List)
            #
            #    # Close the file object
            #    f_object.close()