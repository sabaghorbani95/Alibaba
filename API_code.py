import hashlib
import hmac
import base64
import requests
import datetime
import time

url='https://192.168.0.1/upload.php/'

gmt_date= datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

bucket = 'econect-bucket-000' #'BUCKET_NAME'

local_file = "test03.jpg"#"LOCAL_FILE_PREUPLOAD"
uri = '/Test001/' + 'test02_2023_2_1.jpg'#'Cloud_PATH_ADDRESS'
sign_uri = '/' + bucket + uri
method = 'PUT'
access_key = 'LTAI5t5mtJbHdu4PWrecUaHA'#'SCCESSKEY'
access_key_secret = 'oczTjFNRcN6Vx5X9UAWbdQqZZnPvYx'#'ACCESSKEYSECRET'
sign_string_prefix = method + "\n\n\n" +gmt_date +"\n" +sign_uri
print(repr(sign_string_prefix))
h=hmac.new(access_key_secret.encode(),sign_string_prefix.encode(),digestmod=hashlib.sha1).digest()

sign = "OSS " + access_key + ":" + base64.b64encode(h).decode()

data = open(local_file,'rb')
headers = {"date":gmt_date,
           "Authorization":sign}

print(headers)
url = 'http://'+ bucket +'.oss-eu-central-1.aliyuncs.com' + uri
print(url)
start = time.time()
r = requests.put(url,headers=headers,data=data)
end = time.time()
print("The oss put run time is:{:.3f}".format(end-start))
print(r.status_code)
print(r.headers)
print(r.url)
print("response body: ",r.text)
