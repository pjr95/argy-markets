from datetime import date, timedelta

class Future:
    ''' Class for modeling futures derivatives
    Attributes
    ==========
    underlyng: str
               name/ticker of the underlying
    maturity: date
              maturity date of the future
    lot: int
         number of units of a financial 
         instrument
    settlement: str
                settlement
    type: str
          future type
    '''
    def __init__(self, underlying, maturity, price = 0, pricing_date = date.today(), lot = 1, settlement = 'cash-settled', 
                type ='financial'):
        self.underlying = underlying
        self.maturity = maturity
        self.price = price
        self.pricing_date = pricing_date
        self.lot = lot
        self.settlement = settlement
        self.type = type
    def implied_rate(self,price_spot, price = None,
                      pricing_date  = None):
        if price == None: price = self.price
        if pricing_date == None: pricing_date = self.pricing_date
        r = pow(price / price_spot, \
               365 / (self.maturity - pricing_date).days) -1

        return r

class Forward:
    ''' Class for modeling futures derivatives
    Attributes
    ==========
    underlyng: str
               name/ticker of the underlying
    maturity: date
              maturity date of the future
    lot: int
         number of units
    settlement: str
                settlement
    ''' 
    def __init__(self, underlying, maturity, lot, settlement = "cash-settled"):
        self.underlying = underlying
        self.maturity = maturity
        self.lot = lot
        self.settlement = settlement
    