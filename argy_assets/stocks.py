from datetime import date

class Stock():
    ''' Class for modeling stocks
    Attributes
    ==========
    ticker: str
            stock ticker
    price: float
           stock price
    lot: int
         quoting lot
    g: float
       dividend rate    
    '''
    def __init__(self, ticker, price, lot = 1, g = 0):
        self.ticker = ticker
        self.price = price
        self.lot = lot
        self.g = g

class Cedear(Stock):
      def __init__(self, ticker,  price, foreign_ticker = '', 
                   foreign_market = '', foreign_price = 0, lot = 1, g = 0):
          super().__init__(ticker,  price, lot, g)
          self.foreign_ticker = foreign_ticker 
          self.foreign_market = foreign_market
          self.foreign_price = foreign_price 