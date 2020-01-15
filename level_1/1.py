#!/usr/bin/python3
import requests
input = {'id': 1188, 'holdthedoor': 'Submit'}
URL = 'http://158.69.76.135/level1.php'
for var1 in range (0, 4096):
    requests.post(URL, input)
print("{}".format(var1))
