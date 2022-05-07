import json
import os
from getpass import getpass
from pprint import pprint

import pandas as pd
import requests


class UserProfile:

    def __init__(self):
        self.USERNAME = ''
        self.PASSWORD = ''
        self.API_KEY = ''
        self.TOKEN = ''
        self.REFRESH_TOKEN = ''

    def get_access_token(self):

        # Clear Screen
        try:
            os.system('clear')
        except:
            os.system('cls')
        else:
            pass

            # User params
            URL = 'https://api.invertironline.com/token'
            self.USERNAME = input(f'IOL username: ')
            self.PASSWORD = getpass(f'IOL Password for {self.USERNAME}: ')

            data = {"username": self.USERNAME,
                    "password": self.PASSWORD,
                    "grant_type": "password"
                    }

            response = requests.post(URL, data=data)

            if response.status_code == 200:
                response = response.json()
                self.TOKEN = response.get('access_token')
                self.REFRESH_TOKEN = response.get('refresh_token')

            return response

    def __repr__(self):
        return f'Username: {self.USERNAME}\n' \
               f'Token: {self.TOKEN}'

    def refresh_token(self):
        # User params
            URL = 'https://api.invertironline.com/token'

            data = {"refresh_token": self.REFRESH_TOKEN,
                    "grant_type": "refresh_token"
                    }

            response = requests.post(URL, data=data)

            if response.status_code == 200:
                response = response.json()
                self.TOKEN = response.get('access_token')
                self.REFRESH_TOKEN = response.get('refresh_token')

            return response

    
    def get_options(self, symbol):
        market = 'bCBA'
        URL = f'https://api.invertironline.com/api/v2/{market}/Titulos/{symbol}/Opciones'
        
        payload = {
            'api_key': self.TOKEN,
            "mercado": market,
            "model.mercado": market,
            "simbolo": symbol,
            "model.simbolo": symbol

        }

        headers = {
                'Authorization': f'Bearer {self.TOKEN}',
                'Content-Type': 'application/json'
        }

        response = requests.get(URL,data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response = response.json()
            option_names = []
            for i in response:
                option_names.append(i.get('simbolo'))

        return option_names 

    def get_detailed_data(self, symbol, plazo):
        market = 'bCBA'
        URL = f'https://api.invertironline.com/api/v2/{market}/Titulos/{symbol}/CotizacionDetalle'

        payload = {
            'api_key': self.TOKEN,
            "mercado": market,
            "model.mercado": market,
            "simbolo": symbol,
            "model.simbolo": symbol,
            "plazo": plazo,
            "model.plazo": plazo

        }

        headers = {
            'Authorization': f'Bearer {self.TOKEN}',
            'Content-Type': 'application/json'
        }

        response = requests.get(URL,data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response = response.json()
            apertura = response.get('apertura')
            maximo = response.get('maximo')
            minimo = response.get('minimo')
            tendencia = response.get('tendendcia')
            ultimo_precio = response.get('ultimoPrecio')
            variacion = response.get('variacion')
            cierre = response.get('cierreAnterior')
            monto = response.get('montoOperado')
            volumen = response.get('volumenNominal')

            #print(f'=== {symbol} ==================================')
            #print(f"Open: ${apertura}\tMax: ${maximo}\tMin: {minimo}\t"
            #     f"\nLast: ${ultimo_precio}\tTrend: {'UP' if tendencia == 'sube' else 'DOWN'}"
            #     f"\tVar: {variacion}%\t Cierre Anterior: ${cierre} ")

        else:
            print(response.text)

        return response

    def get_data(self, symbol, plazo):
        
        market = 'bCBA'
        URL = f'https://api.invertironline.com/api/v2/{market}/Titulos/{symbol}/Cotizacion'

        payload = {
            'api_key': self.TOKEN,
            "mercado": market,
            "model.mercado": market,
            "simbolo": symbol,
            "model.simbolo": symbol,
            "plazo": plazo,
            "model.plazo": plazo

        }

        headers = {
            'Authorization': f'Bearer {self.TOKEN}',
            'Content-Type': 'application/json'
        }

        response = requests.get(URL,data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            response = response.json()
            apertura = response.get('apertura')
            maximo = response.get('maximo')
            minimo = response.get('minimo')
            tendencia = response.get('tendendcia')
            ultimo_precio = response.get('ultimoPrecio')
            variacion = response.get('variacion')
            cierre = response.get('cierreAnterior')
            monto = response.get('montoOperado')
            volumen = response.get('volumenNominal')

            #print(f'=== {symbol} ==================================')
            #print(f"Open: ${apertura}\tMax: ${maximo}\tMin: {minimo}\t"
            #     f"\nLast: ${ultimo_precio}\tTrend: {'UP' if tendencia == 'sube' else 'DOWN'}"
            #     f"\tVar: {variacion}%\t Cierre Anterior: ${cierre} ")

        else:
            print(response.text)

        return response
