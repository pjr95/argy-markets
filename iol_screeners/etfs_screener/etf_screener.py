import finnhub
import sys

sys.path.append("../..")
import iol_screeners.client_iol as iol
import argy_assets.etfs as etf

def etf_data(dictionary):
    data = {}
    try:
        for key in dictionary:
            data[key] = finnhub_client.quote(key[:-1])



with open("../keypar") as keys:
    lines = keys.readlines()
    user = lines[0].replace("\n", "")
    password = lines[2].replace("\n", "")

finnhub_client = finnhub.Client(api_key=password)

etf_list = ["SPY", "QQQ", "IWM", "EEM", "XLF", "XLE", "DIA", "EWZ", "ARKK"]

ratios = [20, 20, 10, 5, 2, 2, 20, 2, 10]

etfs_cedear  = {ticker[0] + 'D' : etf.CedearEtf(ticker[0] + 'D' ,ticker[1], ticker[0] ) for ticker in zip(etf_list,ratios)}



print(finnhub_client.quote("SPY"))
