import numpy as np
from pyxirr import xirr
from datetime import date, datetime, timedelta

class BondCashFlow:
    ''' Class for modeling cash-flows.
    Attributes
    ==========
    date: list of dates
          pricing/issue date
    rent: list of floats
          bond rent
    amortisation: list of floats
                  capital amortisation
    netflow: list of floats
             contains the price paid  
             the rent, and the amortisation (element-wise sum)
    couponrate: list of floats
                coupon rate for each period
    residualvalue: list of floats
                    residual value of the bond
                    after each payment date 
    currency: str
              currency of the cash flow
    '''
    def __init__(self,date, rent, amortisation,netflow, couponrate, residualvalue, currency = 'USD'):
        self.date = date
        self.rent = rent
        self.amortisation = amortisation
        self.netflow = netflow
        self.couponrate = couponrate
        self.residualvalue = residualvalue
        self.currency = currency

class SovereignBond:
    ''' Class for modeling soverign bonds
    Attributes
    ==========
    ticker: str
            bond ticker
    cashflow: class BondCashFlow
             contains the cash flow of  
             the bond
    maturity: date
              maturity date    
    series: str
            series of the bond
    country: str
             contry that issued the bond      
    currency: str
              currency of the bond
    periodicity: str
                 periodicity of the payments
    position: int
              position size and direction 
              (negative for short, positive for long,
              zero if you do not have the bond in your
              portfolio) 
    '''
    def __init__(self, ticker, cashflow, maturity, series, country = 'Argentina',
                 currency = 'USD', periodicity = 'semestral', position = 0):
        self.ticker = ticker
        self.cashflow = cashflow
        self.maturity = maturity
        self.series = series
        self.country = country
        self.currency = currency
        self.periodicity = periodicity
        self.position = position

    def buy(self, qty = 1, buying_price = 100):
        if qty < 0: return print('Negative quantities are sells!')
        self.position = self.position + qty 
        self.last_buying_price = buying_price 
        try:
            eval('self.fills')
            self.fills += [(qty, buying_price, datetime.now())]
        except AttributeError:
            self.fills  = [(qty, buying_price, datetime.now())]
        return print(f'Bought {self.ticker} {qty}@{buying_price} {self.currency}' )
    
    def sell(self, qty = -1, selling_price = 100):
        if qty > 0: return print('Positive quantities are buys!')
        self.position = self.position + qty 
        self.last_selling_price = selling_price 
        try:
            eval('self.fills')
            self.fills += [(qty, selling_price, datetime.now())]
        except AttributeError:
            self.fills  = [(qty, selling_price, datetime.now())]       
        return print(f'Sold {self.ticker} {qty}@{selling_price} {self.currency}' )
    
    def wap(self):
        try:
            wap_buy = 0
            wap_sell = 0
            buys = [x[0] for x in self.fills if x[0] > 0]
            sells = [x[0] for x in self.fills if x[0] < 0]
            weight_buy = [x/sum(buys) for x in buys]
            weight_sell = [x/sum(sells)for x in sells]
            price_buy = [x[1] for x in self.fills if x[0] > 0]
            price_sell = [x[1] for x in self.fills if x[0] < 0]
            if weight_buy != [] and weight_sell != []:
                wap_buy = round(np.average(price_buy, weights = weight_buy),2)
                wap_sell = round(np.average(price_sell, weights = weight_sell),2)
            elif weight_buy != []:
                wap_buy = round(np.average(price_buy, weights = weight_buy),2)
            elif weight_sell != []:
                wap_sell = round(np.average(price_sell, weights = weight_sell),2)
            if self.position >= 0:
                position_price = wap_buy
            else:
                position_price = wap_sell
            self.summary = {'Long' : (sum(buys),wap_buy), 
                            'Short' : (sum(sells),wap_sell),
                            'Net' : (self.position, position_price)}
            return {'Long' : wap_buy, 'Short' : wap_sell}
        except AttributeError:
            return print('No positions')

    def ytm(self,price,pricing_date = date.today()):
        today = date.today()
        if pricing_date != date.today():
            settle_date = date.fromisoformat(pricing_date)
        else:
            settle_date = pricing_date
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < today:
            del dates_bond[0]
            del cf[0]
        dates_bond.insert(0, settle_date)
        cf.insert(0, -price)
        ytm = xirr(dates_bond,cf)
        return ytm

    def price(self,ytm,pricing_date = date.today(), rnd = True):
        today = date.today()
        if pricing_date != date.today():
            settle_date = date.fromisoformat(pricing_date)
        else:
            settle_date = pricing_date
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < today:
            del dates_bond[0]
            del cf[0]
        price = 0
        dates_bond.insert(0, settle_date)
        cf.insert(0, price)
        for i in range(1,len(dates_bond)):
            time_left = dates_bond[i] - dates_bond[0]
            time_left = time_left.days/365
            nflow = cf[i]/pow(1 + ytm, time_left)
            price = price + nflow
        if rnd == True:
            return round(price,2)
        else:
            return(price)

    def durations(self,price, pricing_date = date.today ()):
        if pricing_date != date.today():
            settle_date = date.fromisoformat(pricing_date)
        else:
            settle_date = pricing_date
        ytm = self.ytm(price,pricing_date = settle_date)
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < settle_date:
            del dates_bond[0]
            del cf[0]
        cf.insert(0, price)   
        dates_bond.insert(0, settle_date)
        wxt= [None] * (len(dates_bond) - 1)
        for i in range(1,len(dates_bond)):
            time_left = dates_bond[i] - dates_bond[0]
            time_left = time_left.days/365
            wxt[i-1] = (1/price) * (cf[i]/pow(1 + ytm, time_left)) * time_left
        durations = {}
        durations['Macaulay Duration'] = sum(wxt)
        durations['Modified Duration'] = durations['Macaulay Duration'] / (1 + ytm/2)
        durations['$Duration'] = durations['Modified Duration'] * price
        durations['DV01'] = durations['$Duration'] / 10000
        return durations
    
    def convexity(self, price, pricing_date = date.today ()):
        if pricing_date != date.today():
            settle_date = date.fromisoformat(pricing_date)
        else:
            settle_date = pricing_date
        ytm = self.ytm(price,pricing_date = settle_date)
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < settle_date:
            del dates_bond[0]
            del cf[0]
        cf.insert(0, price)   
        dates_bond.insert(0, settle_date)
        wxt= [None] * (len(dates_bond) - 1)
        for i in range(1,len(dates_bond)):
            time_left = dates_bond[i] - dates_bond[0]
            time_left = time_left.days/365
            wxt[i-1] = ((time_left * (time_left + 1) * cf[i]) / \
                         pow(1 + ytm,time_left)) * pow(pow(1 + ytm, 2), -1)
        convexity = {}
        convexity['$Convexity'] = sum(wxt)
        convexity['Convexity'] = convexity['$Convexity'] * \
                                   pow(price, -1) * pow(2,-1)
        return convexity

    def finish_trading(self):
            with open('fills.csv', 'w') as fill:
                for i in self.fills:
                    fill.write(f'{self.ticker};{i[0]};{i[1]}; {i[2]} \n')
            self.position = 0
            try:
                delattr(self, 'fills')
                delattr(self, 'summary')
            except AttributeError:
                pass
