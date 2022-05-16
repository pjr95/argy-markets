import pandas as pd
from datetime import date, datetime
from datetime import date, datetime
from math import log, sqrt, exp, pi
from scipy import stats
from scipy.optimize import fsolve


class call_option(object):
    ''' Class for European call options in BSM Model.
    Attributes
    ==========
    S0: float
        initial stock/index level
    K: float
        strike price
    t: datetime/Timestamp object
        pricing date
    M: datetime/Timestamp object
        maturity date
    r: float
        constant risk-free short rate
    sigma: float
        volatility factor in diffusion term
    Methods
    =======
    value: float
        return present value of call option
    vega: float
        return vega of call option
    imp_vol: float
        return implied volatility given option quote
    '''

    def __init__(self, S0, K, t, M, r, sigma):
        self.S0 = float(S0)
        self.K = K
        self.t = t
        self.M = M
        self.r = r
        self.sigma = sigma

    def update_ttm(self):
        ''' Updates time-to-maturity self.T. '''
        if self.t > self.M:
            raise ValueError("Pricing date later than maturity.")
        self.T = (self.M - self.t).days / 365.

    def d1(self):
        ''' Helper function. '''
        d1 = ((log(self.S0 / self.K)
               + (self.r - self.r + 0.5 * self.sigma ** 2) * self.T)
              / (self.sigma * sqrt(self.T)))
        return d1

    def d2(self):
        ''' Helper function. '''
        d2 = ((log(self.S0 / self.K)
               + (self.r -self.r - 0.5 * self.sigma ** 2) * self.T)
              / (self.sigma * sqrt(self.T)))
        return d2

    def value(self):
        ''' Return option value. '''
        self.update_ttm()
        d1 = self.d1()
        d2 = ((log(self.S0 / self.K)
               + (self.r - self.r - 0.5 * self.sigma ** 2) * self.T)
              / (self.sigma * sqrt(self.T)))
        value = (self.S0 * exp(-self.r * self.T) *stats.norm.cdf(d1, 0.0, 1.0)
                 - self.K * exp(-self.r * self.T) * stats.norm.cdf(d2, 0.0, 1.0))
        return value

    def delta(self):
        ''' Return Delta of option. '''
        self.update_ttm()
        d1 = self.d1()
        delta = stats.norm.cdf(d1, 0.0, 1.0)
        return delta

    def vega(self):
        ''' Return Vega of option. '''
        self.update_ttm()
        d1 = self.d1()
        vega = self.S0 * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(self.T)
        return vega
    
    def theta(self):
        ''' Return Theta of option. '''
        self.update_ttm()
        d1 = self.d1()
        d2 = self.d2()
        theta = (-(self.S0 * stats.norm.pdf(d1, 0.0, 1.0) *self.sigma)/(2 * sqrt(self.T))
                - self.r * self.K * exp(-self.r * self.T) * stats.norm.cdf(d2, 0.0, 1.0))
        return theta
    
    def gamma(self):
        ''' Return Gamma of option. '''
        self.update_ttm()
        d1 = self.d1()
        gamma = stats.norm.pdf(d1, 0.0, 1.0) /(self.S0 * self.sigma * sqrt(self.T))
        return gamma
    
    def rho(self):
        ''' Tho Gamma of option. '''
        self.update_ttm()
        d2 = self.d2()
        rho = self.K * self.T * exp(-self.r * self.T) * stats.norm.cdf(d2, 0.0, 1.0)
        return rho

    def imp_vol(self, C0, sigma_est=0.2):
        ''' Return implied volatility given option price. '''
        option = call_option(self.S0, self.K, self.t, self.M,
                             self.r, sigma_est)
        option.update_ttm()
        
        def difference(sigma):
            option.sigma = sigma
            return option.value() - C0

        iv = fsolve(difference, sigma_est)[0]
        return iv


class put_option(object):
    ''' Class for European put options in BSM Model.
    Attributes
    ==========
    S0: float
        initial stock/index level
    K: float
        strike price
    t: datetime/Timestamp object
        pricing date
    M: datetime/Timestamp object
        maturity date
    r: float
        constant risk-free short rate
    sigma: float
        volatility factor in diffusion term
    Methods
    =======
    value: float
        return present value of call option
    vega: float
        return vega of call option
    imp_vol: float
        return implied volatility given option quote
    '''

    def __init__(self, S0, K, t, M, r, sigma):
        self.S0 = float(S0)
        self.K = K
        self.t = t
        self.M = M
        self.r = r
        self.sigma = sigma

    def update_ttm(self):
        ''' Updates time-to-maturity self.T. '''
        if self.t > self.M:
            raise ValueError("Pricing date later than maturity.")
        self.T = (self.M - self.t).days / 365.

    def d1(self):
        ''' Helper function. '''
        d1 = ((log(self.S0 / self.K)
               + (self.r - self.r + 0.5 * self.sigma ** 2) * self.T)
              / (self.sigma * sqrt(self.T)))
        return d1
    
    def d2(self):
        ''' Helper function. '''
        d2 = ((log(self.S0 / self.K)
               + (self.r -self.r - 0.5 * self.sigma ** 2) * self.T)
              / (self.sigma * sqrt(self.T)))
        return d2

    def value(self):
        ''' Return option value. '''
        self.update_ttm()
        d1 = self.d1()
        d2 = self.d2()
        value = (self.K * exp(-self.r * self.T) * stats.norm.cdf(-d2, 0.0, 1.0)
                 - exp(-self.r * self.T) * self.S0 * stats.norm.cdf(-d1, 0.0, 1.0))
        return value

    def delta(self):
        ''' Return Delta of option. '''
        self.update_ttm()
        d1 = self.d1()
        delta = stats.norm.cdf(d1, 0.0, 1.0) - 1
        return delta
    
    def vega(self):
        ''' Return Vega of option. '''
        self.update_ttm()
        d1 = self.d1()
        vega = self.S0 * stats.norm.pdf(d1, 0.0, 1.0) * sqrt(self.T)
        return vega
    
    def theta(self):
        ''' Return Theta of option. '''
        self.update_ttm()
        d1 = self.d1()
        d2 = self.d2()
        theta = (-(self.S0 * stats.norm.pdf(d1, 0.0, 1.0) *self.sigma)/(2 * sqrt(self.T))
                + self.r * self.K * exp(-self.r * self.T) * stats.norm.cdf(-d2, 0.0, 1.0))
        return theta
    
    def gamma(self):
        ''' Return Gamma of option. '''
        self.update_ttm()
        d1 = self.d1()
        gamma = stats.norm.pdf(d1, 0.0, 1.0) /(self.S0 * self.sigma * sqrt(self.T))
        return gamma
    
    def rho(self):
        ''' Tho Gamma of option. '''
        self.update_ttm()
        d2 = self.d2()
        rho = - self.K * self.T * exp(-self.r * self.T) * stats.norm.cdf(-d2, 0.0, 1.0)
        return rho
    
    def imp_vol(self, C0, sigma_est=0.2):
        ''' Return implied volatility given option price. '''
        option = put_option(self.S0, self.K, self.t, self.M,
                            self.r, sigma_est)
        option.update_ttm()

        def difference(sigma):
            option.sigma = sigma
            return option.value() - C0

        iv = fsolve(difference, sigma_est)[0]
        return iv   

def atm_opt(data,S0):
    '''Returns the ATM strike giving the price of the stock and a list or series of strikes'''
    
    n_upper = [x for x in data if x > S0]
    
    n_lower = [x for x in data if x <= S0]
    
    min_upper = min(n_upper)
    
    max_lower = max(n_lower)
    
    if S0-max_lower > min_upper-S0:
        
        atm_strike = min_upper
        
    else:
        
        atm_strike = max_lower
    
    return(atm_strike)