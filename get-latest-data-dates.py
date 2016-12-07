#!/usr/bin/env python3
import beehive
import json


for node in beehive.get_nodes():
    try:
        r = beehive.get_node_data_dates(node['id'])
    except RuntimeError:
        continue

    if len(r['dates']) == 0:
        continue

    node['dataset_version'] = r['version']
    node['dataset_latest'] = max(r['dates'])
    print(json.dumps(node), flush=True)
