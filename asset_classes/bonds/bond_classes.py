from pyxirr import xirr
from datetime import date, timedelta

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
    maturity: date
              maturity date
    country: str
             contry that issued the bond
    currency: str
              currency of the bond
    series: str
            series of the bond
    cashflow: class BondCashFlow
             contains the cash flow of  
             the bond
    periodicity: str
                 periodicity of the payments
    '''
    def __init__(self,maturity,country,currency,series,cashflow,periodicity):
        self.maturity = maturity
        self.country = country
        self.currency = currency
        self.series = series
        self.cashflow = cashflow
        self.periodicity = periodicity
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


