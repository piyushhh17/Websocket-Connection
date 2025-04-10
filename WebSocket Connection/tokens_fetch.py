import csv
import time
import traceback

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import traceback
from copy import deepcopy

from kiteconnect import KiteConnect

from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
warnings.filterwarnings('ignore')
import math
import redis
import six
import sys
import time
import json
import struct
import logging
import threading
from datetime import datetime, timedelta
from access_token import access_token
# from .__version__ import __version__, __title__
kite = KiteConnect(api_key='c1zwly326w2c7wrj')
kite.set_access_token(access_token)

def instrumentLookup(symbol):
    global access_token, key_secret, kite, instrument_df, tickers, quantity
    try:
        return instrument_df[instrument_df.tradingsymbol == symbol].instrument_token.values[0]
    except:
        return -1


def getInstruments():
    global access_token, key_secret, kite, instrument_df, tickers, quantity
    while True:
        try:
            instrument_dump = kite.instruments()
            instrument_df = pd.DataFrame(instrument_dump)
            break
        except Exception as e:
            print(str(e))
            continue
getInstruments()

def get_atm_nifty(ltp):
    nifty_step_size = 50
    mod = math.fmod(ltp, nifty_step_size)
    if mod >= 25:
        atm_value = ltp - mod + nifty_step_size
    else:
        atm_value = ltp - mod
    #print('Nifty ATM Value: ', int(atm_value))
    return int(atm_value)

def get_atm_bank_nifty(ltp):
    bnf_step_size = 100
    mod = math.fmod(ltp, bnf_step_size)
    if mod > 50:
        atm_value = int((ltp//100)*100)+100
    else:
        atm_value = int(ltp//100)*100
    return atm_value
    

def fetch_ltp(kite, name):
    '''
    Function takes kite object, name of exchange and name of instruments
    and returns the ltp
    '''
    instrument_name = str(instrumentLookup(name))
    
    ltp = kite.ltp(instrument_name)[instrument_name]['last_price']
    return ltp
nifty_df = instrument_df[(instrument_df['name'] == 'NIFTY') & (instrument_df['instrument_type'] == 'CE')& (instrument_df['strike'] == (get_atm_nifty(fetch_ltp(kite, 'NIFTY 50'))))]
nifty_df = nifty_df.head(3)
# 15 itm/otm CE
for i in range(-15, 15):
    temp_df = instrument_df[(instrument_df['name'] == 'NIFTY') & (instrument_df['instrument_type'] == 'CE')& (instrument_df['strike'] == (get_atm_nifty(fetch_ltp(kite, 'NIFTY 50'))) + (50*i))]
    temp_df = temp_df.head(3)
    nifty_df = pd.concat([nifty_df, temp_df], ignore_index=True)
nifty_df_pe = instrument_df[(instrument_df['name'] == 'NIFTY') & (instrument_df['instrument_type'] == 'PE')& (instrument_df['strike'] == (get_atm_nifty(fetch_ltp(kite, 'NIFTY 50'))))]
nifty_df_pe = nifty_df_pe.head(3)
# 15 itm/otm PE
for i in range(-15, 15):
    temp_df_pe = instrument_df[(instrument_df['name'] == 'NIFTY') & (instrument_df['instrument_type'] == 'PE')& (instrument_df['strike'] == (get_atm_nifty(fetch_ltp(kite, 'NIFTY 50'))) + (50*i))]
    temp_df_pe = temp_df_pe.head(3)
    nifty_df_pe = pd.concat([nifty_df_pe, temp_df_pe], ignore_index=True)

nifty_df = pd.concat([nifty_df, nifty_df_pe], ignore_index=True)
token_list = nifty_df['instrument_token'].tolist()
print(token_list)