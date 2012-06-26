
import time
import base64
from M2Crypto import RSA
import httplib, urllib
import json
  

 
username = 'username'
password = 'password'
service  = 'NEXTAPI'
URL='api.test.nordnet.se'
BASE_URL='api.test.nordnet.se/next'
API_VERSION='1'
 
timestamp = int(round(time.time()*1000))
timestamp = str(timestamp)
buf = base64.b64encode(username) + ':' + base64.b64encode(password) + \
    ':' + base64.b64encode(timestamp)
rsa = RSA.load_pub_key('NEXTAPI_TEST_public.pem')
encrypted_hash = rsa.public_encrypt(buf, RSA.pkcs1_padding)
hash = base64.b64encode(encrypted_hash)
 
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    'Accept-Language':'en'
    }
conn = httplib.HTTPSConnection(URL)
 
# GET server status
conn.request('GET','https://'+BASE_URL+'/'+API_VERSION, '', headers)
r=conn.getresponse()
response=r.read()
j = json.loads(response)
print_json(j)
 
# POST login
params = urllib.urlencode({'service': 'NEXTAPI', 'auth': hash})
conn.request('POST',
             'https://' + BASE_URL + '/' + API_VERSION + '/login',
             params,headers)
r=conn.getresponse()
response=r.read()
j = json.loads(response)
print_json(j)
