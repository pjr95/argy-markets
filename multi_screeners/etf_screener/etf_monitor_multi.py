import yfinance as yf
import investpy as inv
import pandas as pd
import xlwings as xw
from datetime import datetime, date

etfs = 'ARKK DIA EEM EWZ IWM QQQ SPY XLE XLF'
wb = xw.Book('MonitorETF.xlsx')
sheet1 = wb.sheets['ETF-USA']

while True:
    try:
        etf_info = yf.Tickers(etfs) #Tengo que conectarme cada 
        df = pd.DataFrame(columns =['Price','Previous Close', 'Max Price', '1y High'], 
                          index = ['ARKK', 'DIA', 'EEM', 'EWZ', 'IWM', 'QQQ', 'SPY', 'XLE', 'XLF'])
        index_info = inv.indices.get_indices_overview('united states', as_json=False, n_results=4)
        #sp500 = index_info[index_info['name'] == 'S&P 500']
        #nasdaq = index_info[index_info['name'] == 'Nasdaq100']   
        for i in ['ARKK', 'DIA', 'EEM', 'EWZ', 'IWM', 'QQQ', 'SPY', 'XLE', 'XLF']:
            maxPrice = max(etf_info.tickers[i].history(period = 'max')['Close'])
            etfPrice = etf_info.tickers[i].info['regularMarketPrice']
            previousClose = etf_info.tickers[i].info['regularMarketPreviousClose']
            high1y = max(etf_info.tickers[i].history(period='1y')['Close'])
            price = [etfPrice, previousClose,maxPrice,high1y]
            df.loc[i] = price     
        sheet1.range('A1').value = df
        sheet1.range('A12').value = index_info
        sheet1.range('A18').value = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
        print('Up and running')
    except AttributeError:
        continue