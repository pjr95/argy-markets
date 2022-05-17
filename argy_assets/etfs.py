from datetime import date

class Etf():
    ''' Class for modeling Exchange Traded Funds
    Attributes
    ==========
    ticker: str
            etf ticker
    price: float
           etf price
    ratio: int
           ratio of Cedears that form one 
           stock in the original exchange
    foreign_ticker: str
                    original etf ticker
    foreign_market: str
                    name of the original exchange
                    where the etf is listed
    '''
    def __init__(self, ticker, price, ratio, foreign_ticker, foreign_market):
        self.ticker = ticker
        self.price = price
        self.ratio = ratio
        self.foreign_ticker = foreign_ticker
        self.foreign_market = foreign_market