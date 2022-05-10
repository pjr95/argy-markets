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
