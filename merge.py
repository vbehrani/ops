#!/usr/bin/env python3
import fileinput
import json


results = {}

for item in map(json.loads, fileinput.input()):
    r = results.get(item['id'], {})
    r.update(item)
    results[item['id']] = r


for item in results.values():
    print(json.dumps(item))


# def ssh_alive(r):
#     return r['ssh_alive']
#
#
# def data_latest(r):
#     return r['data_latest']
#
# # pprint(sorted(filter(ssh_alive, results), key=data_latest))
