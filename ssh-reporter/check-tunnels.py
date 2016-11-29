import requests
import subprocess
from datetime import datetime


r = requests.get('http://beehive1.mcs.anl.gov/api/nodes')
nodes = r.json()

status = []

for node in nodes:
    nodeid = node['id']
    port = node['port']
    try:
        subprocess.check_output("ssh node{} 'echo OK; exit'".format(port), shell=True)
        status.append((nodeid, 'OK'))
    except:
        status.append((nodeid, 'ERR'))

filename = datetime.now().strftime('ssh-%Y%m%d%H%M%S.csv')

with open(filename, 'w') as f:
    for line in status:
        f.write(','.join(line) + '\n')
