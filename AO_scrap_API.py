import requests
import time
from fake_useragent import UserAgent
import random
import subprocess
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes
import json
import base64
from datetime import datetime

from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import json
# def format_js_timestamp_to_date(timestamp):
#     """
#     Converts a JavaScript timestamp (milliseconds since the epoch) to a formatted date string.

#     Args:
#     - timestamp (int): The JavaScript timestamp in milliseconds.

#     Returns:
#     - str: The formatted date string.
#     """
#     # Convert the timestamp from milliseconds to seconds
#     timestamp_seconds = timestamp / 1000.0

#     # Create a datetime object from the timestamp
#     dt = datetime.fromtimestamp(timestamp_seconds)

#     # Format the datetime object as a string
#     # Customize the format string as needed
#     formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')

#     return formatted_date
def formatDate(t):
    # Convert milliseconds to seconds for Python datetime
    t_datetime = datetime.fromtimestamp(t / 1000)
    
    # Get the current timezone offset in hours
    timezone_offset = datetime.now().astimezone().utcoffset()
    
    # Correctly apply the timezone offset
    adjusted_datetime = t_datetime + timezone_offset
    
    n = adjusted_datetime.day
    r = int(str(n).zfill(2)[::-1])
    i = adjusted_datetime.year
    a = int(str(i)[::-1])
    o = hex(int(t)).lstrip('0x') + str((i + a) * (n + r))
    o = o[:14] if len(o) > 14 else o.ljust(14, '0')
    
    return "#" + o + "$"
def format_date(t):
    e = -datetime.now().astimezone().utcoffset().total_seconds() / 60
    n_date = t + timedelta(minutes=e * 60)
    n = n_date.day
    r = int(f"{n:02d}"[::-1])
    i = t.year
    a = int(str(i)[::-1])
    o = int(f"{t.timestamp():.0f}", 16)
    o_str = f"{o:x}" + str((i + a) * (n + r)).encode('utf-8').hex()
    o_len = len(o_str)
    
    if o_len < 14:
        o_str += "0" * (14 - o_len)
    else:
        o_str = o_str[:14]
    
    return "#" + o_str + "$"
def base16_to_base36(hex_num):
    # Convert base-16 to decimal first
    decimal_num = int(hex_num, 16)
    # Now convert decimal to base-36
    base36_num = ''
    # alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

    while decimal_num > 0:
        decimal_num, i = divmod(decimal_num, 36)
        base36_num = alphabet[i] + base36_num

    return base36_num

def format_date_py(timestamp):
    """Format the date in a specific way based on the provided JavaScript logic."""
    # Convert timestamp to datetime
    
    dt = datetime.utcfromtimestamp(timestamp / 1000)
    timeZoneOffset = 180 # e
    
    
    # print("e format: ", {dt.isoformat()}+00:00)
    print(f"UTC datetime: {dt.isoformat()}+00:00")
    # Extract components
    day = dt.day # n
    print("day n: ", day)
    r = int(str(day).zfill(2)[::-1])

    print("r ?: ", r) # r
    year = dt.year # i
    print("year i: ", year)

    # Reverse day and year, then perform calculations
    reversed_day = int(str(day)[::-1])
    
    
    reversed_year = int(str(year)[::-1]) # a

    print("reverse year1: ", str(year)[::-1])
    print("reverse year: ", reversed_year)
    o_base36 = base16_to_base36(str(timestamp))
    print("obase36: ", o_base36)
# Calculate arithmetic operation and convert to custom base (here using base 24 as an example)
    
    calc_base24 = custom_base24encode((year + reversed_year) * (day + r))
    print("calcbase24: ", calc_base24)
    
    ofinal = o_base36 + calc_base24
    
    stringLen =  len(ofinal) # s string lenth
    
    if (stringLen < 14):
        c = 0
        for c in range(14 - stringLen):
            o += "0"
    else:
        # stringLen > 14 && (o_base36)
        ofinal = ofinal[:14]

    # Convert timestamp to base 36
    # timestamp_base36 = base36_encode(int(timestamp / 1000))

    # # Perform the calculation for the second part
    # calculation_result = ((year + reversed_year) * (day + reversed_day))
    # calculation_base24 = base36_encode(calculation_result)  # Using base36 as a placeholder for base24

    # Concatenate and adjust the length of the final string


    return f"#{ofinal}$"

def base36encode(number):
    """Converts an integer to a base-36 string."""
    assert number >= 0, 'positive integer required'
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = ''
    while number:
        number, rem = divmod(number, 36)
        res = digits[rem] + res
    return res or '0'

def custom_base24encode(number):
    """A custom base 24 encoding. Adjust this function based on your needs."""
    assert number >= 0, 'positive integer required'
    digits = '0123456789abcdefghijklm'
    res = ''
    while number:
        number, rem = divmod(number, 24)
        res = digits[rem] + res
    return res or '0'

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

def decrypt_data(data):
    print(data["lastModified"]
    )
    encrypted_response = data["response"]
    last_modified = data["lastModified"]
    

    formatted_date = format_date_py(last_modified)

    
    print("date:", formatted_date)
    
    key = base64.b64encode(formatted_date.encode('utf-8'))[:16]
    print("key:", key)

    iv = base64.b64encode(formatted_date.upper().encode('utf-8'))[:16]
    print("iv:", iv)

    
    # Decode the encrypted response
    ct_bytes = base64.b64decode(encrypted_response)
    # print("ct_bytes:", ct_bytes)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    # print(cipher.decrypt(ct_bytes))
    # Decrypt and unpad the message
    data_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    data = json.loads(data_bytes.decode('utf-8'))
    return data

# Generate a random user-agent
ua = UserAgent()
headers = {
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Use session object to maintain state across requests
session = requests.Session()

# Mimic human behavior by adding delays
time.sleep(random.uniform(1, 5))

url = 'https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/year/2024/eventId/580/matchId/MS701/pointId/0_0_0'

# url = 'https://itp-ao-sls.infosys-platforms.com/prod/api/court-vision/belowCourt/year/2024/eventId/580/matchId/MS701/pointId/0_0_0'

response = session.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # print(data)  # or process as needed
    data_json = json.dumps(data)
    decrypted_data = decode(data)
    print("Decrypted data:", decrypted_data)
    # result = subprocess.run(['node', 'API_Decryption.js', data_json], capture_output=True, text=True)
    # print(result.stdout)

else:
    print(f"Failed to retrieve data, status code: {response.status_code}")




# def encrypt_data(data, key):
#     # Convert the key to 16 bytes (128 bits)
#     key = key.encode('utf-8')[:16]
#     # Initialize cipher
#     cipher = AES.new(key, AES.MODE_CBC)
#     # Convert data to JSON and then bytes
#     data_bytes = json.dumps(data).encode('utf-8')
#     # Encrypt the data
#     ct_bytes = cipher.encrypt(pad(data_bytes, AES.block_size))
#     # Encode the ciphertext and iv to base64 to make it easy to store and transport
#     ciphertext = base64.b64encode(ct_bytes).decode('utf-8')
#     iv = base64.b64encode(cipher.iv).decode('utf-8')
#     return iv, ciphertext



# Example usage
key = 'secret key 123'
data = {"example": "data"}


