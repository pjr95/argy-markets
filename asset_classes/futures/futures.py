from datetime import date, timedelta

class Future:
    ''' Class for modeling futures derivatives
    Attributes
    ==========
    underlyng: str
               name/ticker of the underlying
    maturity: date
              maturity date of the future
    '''
    def __init__(self, underlying, maturity):
        self.underlying = underlying
        self.maturity = maturity
    def implicit_rate(self,price_future, price_spot,
                      pricing_date = date.today()):
        r = pow(price_future/price_spot, \
        (self.maturity - pricing_date).days/365) -1

        return r