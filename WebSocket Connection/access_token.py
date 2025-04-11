import requests
import pandas as pd
import pyotp
import time
from kiteconnect import KiteConnect
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import requests
from requests.exceptions import Timeout
import json
import time

import streamlit as st
import pandas as pd
creds = {'user_id':'####','password':'#######','totp_key':'########','api_key':'#######', 'api_secret':"#########" }
api_key = 'c1zwly326w2c7wrj'
base_url = "https://kite.zerodha.com"
login_url = "https://kite.zerodha.com/api/login"
twofa_url = "https://kite.zerodha.com/api/twofa"
instruments_url = "https://api.kite.trade/instruments"


session = requests.Session()
response = session.post(login_url,data={'user_id':creds['user_id'],'password':creds['password']})
request_id = json.loads(response.text)['data']['request_id']
twofa_pin = pyotp.TOTP(creds['totp_key']).now()
response_1 = session.post(twofa_url,data={'user_id':creds['user_id'],'request_id':request_id,'twofa_value':twofa_pin,'twofa_type':'totp'})
kite = KiteConnect(api_key=creds['api_key'])
kite_url = kite.login_url()



try:
  session.get(kite_url)
except Exception as e:
  e_msg = str(e)
  #print(e_msg)
  request_token = e_msg.split('request_token=')[1].split(' ')[0].split('&action')[0]
  print('Successful Login with Request Token:{}'.format(request_token))
  st.write("Logged In")

access_token = kite.generate_session(request_token,creds['api_secret'])['access_token']
kite.set_access_token(access_token)


profile = kite.profile()
# st.write(profile)
# st.write("Welcome",profile["user_id"]," ",profile["user_name"])
print(access_token)
