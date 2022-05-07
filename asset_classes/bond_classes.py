from pyxirr import xirr
from datetime import date, timedelta

class BondCashFlow:
    def __init__(self,date, rent, amortisation,netflow, couponrate, residualvalue):
        self.date = date
        self.rent = rent
        self.amortisation = amortisation
        self.netflow = netflow
        self.couponrate = couponrate
        self.residualvalue = residualvalue

class SovereignBond:
    def __init__(self,maturity,country,currency,series,cashflow,periodicity):
        self.maturity = maturity
        self.country = country
        self.currency = currency
        self.series = series
        self.cashflow = cashflow
        self.periodicity = periodicity
    def ytm(self,price,settlementDate = date.today()):
        today = date.today()
        if settlementDate != date.today():
            settle_date = date.fromisoformat(settlementDate)
        else:
            settle_date = settlementDate
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < today:
            del dates_bond[0]
            del cf[0]
        dates_bond.insert(0, settle_date)
        cf.insert(0, -price)
        ytm = xirr(dates_bond,cf)
        return ytm
    def price(self,ytm,settlementDate = date.today(), rnd = True):
        today = date.today()
        if settlementDate != date.today():
            settle_date = date.fromisoformat(settlementDate)
        else:
            settle_date = settlementDate
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
    def durations(self,price,settlementDate,changeytm = 0.01):
        today = date.today()
        if settlementDate != date.today():
            settle_date = date.fromisoformat(settlementDate)
        else:
            settle_date = settlementDate
        cf = list(self.cashflow.netflow)
        dates_bond = list(self.cashflow.date)
        while  dates_bond[0] < today:
            del dates_bond[0]
            del cf[0]
        price = 0
        dates_bond.insert(0, settle_date)
        cf.insert(0, price)
        ytm = self.ytm(price,settlementDate = settle_date)
        wxt= [None] * (len(dates_bond) - 1)
        for i in range(1,len(dates_bond)):
            time_left = dates_bond[i] - dates_bond[0]
            time_left = time_left.days/365
            wxt[i-1] = (1/price) * (cf[i]/pow(1 + ytm, time_left)) * time_left
        durations = {}















'''
class CashFlow:
    def __init__(self,inflows,outflows,rates,period):
        self.inflows = inflows
        self.outflows = outflows
        self.rates = rates
        self.period = period
        self.net_flows = [x + y for x, y in zip(inflows, outflows)]

    def pv(self):
        rho = self.rates + 1
        pv = [x / self.rates for x in self.net_flows]
        return pv
'''


