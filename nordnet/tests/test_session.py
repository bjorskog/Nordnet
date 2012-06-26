# nordnet API test 
# https://api.test.nordnet.se/
import time
import base64
import requests
import json
from M2Crypto import RSA

def print_json(j, prefix=''):
    if prefix == '':
        print '*'*20
    if not isinstance(j,list):
        j = [j]
    for d in j:
        for key, value in d.items():
            if isinstance (value,dict):
                print '%s%s' % (prefix, key)
                print_json(value, prefix+'  ')
            else:
                print '%s%s:%s' % (prefix, key,value)
 
timestamp = int(round(time.time()*1000))
timestamp = str(timestamp)
mylogin, mypassword = ('username', 'password')
login = base64.b64encode(mylogin)
password = base64.b64encode(mypassword)
phrase = base64.b64encode(timestamp)
buf = login + ':' + password + ':' + phrase
rsa = RSA.load_pub_key('../NEXTAPI_TEST_public.pem')
encrypted_hash = rsa.public_encrypt(buf, RSA.pkcs1_padding)
hash = base64.b64encode(encrypted_hash)

BASE_URL = 'api.test.nordnet.se/next'
API_VERSION = '1'
URL = 'https://%s/%s' % (BASE_URL,API_VERSION)

def req(cmd=''):
    r=requests.get(URL + '/%s' % cmd ,auth = auth, headers=headers)
    return json.loads(r.text)

def touch(): 
    requests.put(URL+'/login/%s' % session_key, auth = auth, headers=headers)
 
def logout():    
    r=requests.delete(URL + '/login/%s' % session_key, 
                      auth = auth, headers=headers)
    print_json(json.loads(r.text))
    
def buy(identifier,marketID,price,volume,currency): 
    r = requests.post(URL + '/accounts/%s/orders' % account_id,
                      data={'identifier':identifier,'marketID':marketID,
                            'price':price,'volume':volume,'currency':currency,
                            'side':'buy'}, 
                      auth=auth, headers=headers).text
    return json.loads(r)

def delete_order(order_id): 
    return json.loads(
        requests.delete(
            URL+'/accounts/%s/orders/%s' % (account_id, order_id), 
            auth=auth, headers=headers).text)
 
def f2():
    global headers, params, session_key, auth, account_id
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "application/json",'Accept-Language':'en'}
    params = {'service': 'NEXTAPI', 'auth': hash}
    r = requests.get(URL, headers = headers)
    print_json(json.loads(r.text))
    
    r=requests.post(URL + '/login',data=params, headers=headers)
    print_json(json.loads(r.text))
 
    rj=json.loads(r.text)
    session_key=rj['session_key']
    auth = (session_key,session_key)
    
    print_json(req('accounts'))
    account_id = req('accounts')[0]['id']
    
    print_json(req('accounts/%s' % account_id))
    print_json(req('accounts/%s/ledgers' % account_id))
    print_json(req('accounts/%s/positions' % account_id))
    if 1:
        print_json(req('accounts/%s/orders' % account_id)) # Exchange orders
        print_json(req('accounts/%s/trades' % account_id)) # Exchange trades
        print_json(req('instruments?query=abb&type=A&country=SE'))
        print_json(req('instruments?identifier=101&amp;marketID=11'))
        print_json(req('instruments?list=11,101;11,817;11,939')) 
        print_json(req('chart_data?marketID=11&identifier=101')) 
        # response = u'error': u'Instrument not found'}
        #print_json(req('lists/26'))
        print_json(req('markets'))
        print_json(req('indices'))
        print_json(req('ticksizes/11002'))
        #print_json(req('derivatives/WNT'))
 
        r=buy(101,11,80,2,'SEK')
        print print_json(r)
        print_json(req('accounts/%s/orders' % account_id))
        print_json(delete_order(r['orderID']))
        print_json(req('accounts/%s/orders' % account_id))

f2()
