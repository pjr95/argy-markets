import client_iol as iol
import pandas as pd
import json
import time
import os
import Options_screener.options as opt
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

                strike = int(k[4:7])

                strikes.append(strike)

            strikes = list(set(strikes))
            
            strikes.sort()   

            atm_opt = opt.atm_opt(strikes,ggal_price)

            index_atm = strikes.index(atm_opt)

            neighbours = strikes[index_atm - 5 : index_atm + 5]

            strikes = [x for x in opt_names for y in neighbours if str(y) in x]

            monitor = pd.DataFrame()

            for opt_ticker in strikes:
                try:
                    opt_data = user_pablo.get_detailed_data(opt_ticker, 't1')
                    exp_date = datetime.strptime(opt_data.get('descripcionTitulo')[-10:],
                    '%d/%m/%Y').date()
                    book = pd.DataFrame.from_dict(opt_data.get('puntas')[0], 
                        orient = 'index', columns = [opt_ticker]).transpose()
                    book['Vencimiento'] = exp_date
                    book['Días a Vencimiento'] = (exp_date - date.today()).days
                    strike = int(opt_ticker[4:7])
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
            
            #monitor.to_csv('Monitor-prueba.csv')

            middle = time.time()

            print(middle - start)
        else:

            _ = user_pablo.refresh_token()
            
            middle = 0

end = time.time()
print(end - start)
#    with open('info.json', 'w') as f:
#        json.dump(opt_data, f)
#    with open('info2.json', 'w') as f:
#        json.dump(opt_names, f)
#    info3 = user_pablo.get_data(i, 't1')
#    with open('info3.json', 'w') as f:
#        json.dump(info3, f)
    #print(strikes)
