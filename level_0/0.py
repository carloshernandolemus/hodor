#!/usr/bin/python3
import requests
input = {'id': 344, 'holdthedoor': 'Submit'}
URL = 'http://158.69.76.135/level0.php'
for vote in range (0, 1024):
    requests.post(URL, input)

print("Votes counted:{}".format(vote))
