#!/usr/bin/env python3
import beehive
import json
import time


for node in beehive.get_nodes():
    node['ssh_alive'] = beehive.get_tunnel_status(node['ssh_port'])
    node['ssh_timestamp'] = time.time()
    print(json.dumps(node), flush=True)
