import subprocess
import json


def hastunnel(node):
    return node.get('tunnel') == 'up'


with open('tunnels.json') as f:
    nodes = list(filter(hastunnel, json.load(f)))


for node in nodes:
    with open('reports/{}.txt'.format(node['id']), 'w') as f:
        output = subprocess.check_output("ssh node{} 'curl -s https://gist.githubusercontent.com/seanshahkarami/9fee74fb074da6a97199b4f728e930e5/raw/abc7658dd9b1b404a93948c86d02cd6528445780/Report | /bin/sh'".format(node['port']), shell=True).decode()
        f.write(output)
    print('# {} @ {}'.format(node['id'], node['port']))
    print(output)

# Bus 001 Device 004: ID 2341:8037 Arduino SA - wagman
# Bus 001 Device 003: ID 2341:003e Arduino SA - coresense
# 1bc7:0021 modem
# 04d8:ffee alphasense
