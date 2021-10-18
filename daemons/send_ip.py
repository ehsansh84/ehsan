import requests, os
from consts import consts
API_URL = 'https://api.ehsanshirzadi.com'
url = 'http://icanhazip.com'
result = requests.get(url)
pc_ip = result.text.rstrip('\n')
print(os.path.exists('/var/tmp/ip.txt'))
old_ip = ''
if not os.path.exists('/var/tmp/ip.txt'):
    f = open('/var/tmp/ip.txt', 'w')
    f.write(pc_ip)
    f.close()
else:
    f = open('/var/tmp/ip.txt', 'r')
    old_ip = f.read()
    f.close()

if pc_ip != old_ip:
    SETTING_API = consts.API_URL + '/v1/setting'
    data = {
        'conditions': {'name': 'mypc'},
        'ip': pc_ip
    }
    result = requests.put(SETTING_API, json=data)
