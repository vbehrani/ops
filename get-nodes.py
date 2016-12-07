#!/usr/bin/env python3
import beehive
import json


for node in beehive.get_nodes():
    print(json.dumps(node), flush=True)
