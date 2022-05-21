import pandas as pd
import json
import time
import os
import sys
sys.path.append('../..')
import iol_screeners.client_iol as iol
import argy_assets.options as opt
from pprint import pprint
from datetime import datetime, date, timedelta



start = time.time()

r = 0.33

sigma = 0.39


if __name__ == '__main__':

    user_pablo = iol.UserProfile()

    _ = user_pablo.get_access_token()

    middle = time.time()

    while True:
        if middle - start < 600:

            ggal = user_pablo.get_data('GGAL','t2')

            ggal_price = round(ggal.get('ultimoPrecio'), 2)

            opt_names = user_pablo.get_options('GGAL')

            strikes = []

            for k in opt_names:

                strike = list(map(str,k))

                strike = [i for i in strike if i.isdigit()]

                strike = ''.join(strike)

                strike = int(strike)

                if len(str(strike)) > 4: strike = strike/100

                strikes.append(strike)
            
            strikes.sort()   

            atm_opt = opt.atm_opt(strikes,ggal_price)

            index_atm = strikes.index(atm_opt)

            neighbours = strikes[index_atm - 5 : index_atm + 5]

            for indx, i in enumerate(neighbours):
                if type(i) == float:
                    neighbours[indx] = str(i).replace('.','')

            tickers = [x for x in opt_names for y in neighbours if str(y) in x]

            monitor = pd.DataFrame()

            for opt_ticker in tickers:
                try:
                    opt_data = user_pablo.get_detailed_data(opt_ticker, 't1')
                    exp_date = datetime.strptime(opt_data.get('descripcionTitulo')[-10:],
                    '%d/%m/%Y').date()
                    book = pd.DataFrame.from_dict(opt_data.get('puntas')[0], 
                        orient = 'index', columns = [opt_ticker]).transpose()
                    book['Vencimiento'] = exp_date
                    book['Días a Vencimiento'] = (exp_date - date.today()).days
                    strike = list(map(str,k))
                    strike = [i for i in strike if i.isdigit()]
                    strike = ''.join(strike)
                    strike = int(strike)
                    if opt_ticker[3] == 'C':
                        call_bs = opt.call_option(ggal_price, strike, 
                                          date.today(), exp_date, 
                                          r, sigma)
                        if int(book['precioCompra']) != 0:
                            book['IV Bid'] = call_bs.imp_vol(round(opt_data.get('puntas')[0].get('precioCompra'),2),sigma)
                        else:
                            book['IV Bid'] = 0
                        if int(book['precioVenta']) != 0:
                            book['IV Ask'] = call_bs.imp_vol(round(opt_data.get('puntas')[0].get('precioVenta'),2),sigma)
                        else:
                            book['IV Ask'] = 0
                    else:
                        put_bs = opt.put_option(ggal_price, strike, 
                                          date.today(), exp_date, 
                                          r, sigma)
                        if int(book['precioCompra']) != 0:
                            book['IV Bid'] = put_bs.imp_vol(round(opt_data.get('puntas')[0].get('precioCompra'),2),sigma)
                        else:
                            book['IV Bid'] = 0
                        if int(book['precioVenta']) != 0:
                            book['IV Ask'] = put_bs.imp_vol(round(opt_data.get('puntas')[0].get('precioVenta'),2),sigma)
                        else:
                            book['IV Ask'] = 0
                        
                    monitor = monitor.append(book)
                    del book
                except IndexError:
                    pass

            os.system('cls')

            pprint(monitor)

            middle = time.time()

            print(middle - start)
        else:

            _ = user_pablo.refresh_token()
            
            middle = 0

end = time.time()
print(end - start)
