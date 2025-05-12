import requests
import json
import time
import base64
file = './SM_BS_Staghorn_350cm.png'


with open(file, 'rb') as f:
    image_bytes = f.read()
base64_image = base64.b64encode(image_bytes).decode('utf-8')

headers = {"Content-Type":"application/json"}
data = {
        "request_body": {
            "img": base64_image,
            "use_name": False,
            "file_name" : "test003"
        },
        "session_data" : {}
    }
t1 = time.time()
res = requests.post("http://43.163.45.187:8080/predict/",json=data,headers=headers)
# res = requests.post("http://101.32.173.92:8080/predict/",json=data,headers=headers)
# res = requests.post("http://10.219.156.161:8090/",json=data,headers=headers)
# res = requests.post("http://10.219.156.161:8090/predict/",json=data,headers=headers)
t2 = time.time()
# print(res.json())
data = res.json()

print(data)
print('cost time: %.3f'%(t2-t1))