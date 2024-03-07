import requests
import time
from fake_useragent import UserAgent
import random
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def base16_to_base36(hex_num):
    decimal_num = int(hex_num, 16)
    base36_num = ''
    # alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    while decimal_num > 0:
        decimal_num, i = divmod(decimal_num, 36)
        base36_num = alphabet[i] + base36_num

    return base36_num


def custom_base24encode(number):
    """A custom base 24 encoding. Adjust this function based on your needs."""
    assert number >= 0, 'positive integer required'
    digits = '0123456789abcdefghijklm'
    res = ''
    while number:
        number, rem = divmod(number, 24)
        res = digits[rem] + res
    return res or '0'



def format_date_py(timestamp):
    """Format the date in a specific way based on the provided JavaScript logic."""
    
    dt = datetime.utcfromtimestamp(timestamp / 1000)
    timeZoneOffset = 180 # e
    
    print(f"UTC datetime: {dt.isoformat()}+00:00")

    day = dt.day # n
    print("day n: ", day)
    r = int(str(day).zfill(2)[::-1])

    print("r ?: ", r) # r
    year = dt.year # i
    print("year i: ", year)

    reversed_day = int(str(day)[::-1])
    
    reversed_year = int(str(year)[::-1]) # a

    print("reverse year1: ", str(year)[::-1])
    print("reverse year: ", reversed_year)
    o_base36 = base16_to_base36(str(timestamp))
    print("obase36: ", o_base36)
    
    
    calc_base24 = custom_base24encode((year + reversed_year) * (day + r))
    print("calcbase24: ", calc_base24)
    
    ofinal = o_base36 + calc_base24
    
    stringLen =  len(ofinal) # s string len
    
    if (stringLen < 14):
        c = 0
        for c in range(14 - stringLen):
            o += "0"
    else:
        # stringLen > 14 && (o_base36)
        ofinal = ofinal[:14]

    # calculation_result = ((year + reversed_year) * (day + reversed_day))
    # calculation_base24 = base36_encode(calculation_result) 

    return f"#{ofinal}$"

def decode(data):
    e = format_date_py(data['lastModified'])
    n = e.encode('utf-8')
    r = e.upper().encode('utf-8')
    backend = default_backend()
    cipher = Cipher(algorithms.AES(n), modes.CBC(r), backend=backend)
    decryptor = cipher.decryptor()
    padder = padding.PKCS7(128).unpadder()
    
    decrypted = decryptor.update(base64.b64decode(data['response'])) + decryptor.finalize()
    unpadded = padder.update(decrypted) + padder.finalize()
    
    return json.loads(unpadded.decode('utf-8'))


# random user-agent
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

session = requests.Session()

# Mimic human behavior by adding delays
time.sleep(random.uniform(1, 5))

url = 'https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/year/2024/eventId/580/matchId/MS701/pointId/0_0_0'


response = session.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    data_json = json.dumps(data)
    decrypted_data = decode(data)
    print("Decrypted data:", decrypted_data)

else:
    print(f"Failed to retrieve data, status code: {response.status_code}")
