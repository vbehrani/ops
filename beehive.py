import requests
import subprocess


def get_nodes():
    r = requests.get('http://beehive1.mcs.anl.gov/api/nodes')

    if r.status_code != 200:
        raise RuntimeError('Could not get node list.')

    nodes = r.json()

    for node in nodes:
        yield {
            'id': node['id'][-12:].lower(),
            'name': node['name'],
            'description': node['description'],
            'location': node['location'],
            'ssh_port': node['port'],
        }


def get_node_data_dates(node_id):
    node_id = node_id.rjust(16, '0')

    for version in ['2', '1']:
        r = requests.get('http://beehive1.mcs.anl.gov/api/1/nodes/{}/dates?version={}'.format(node_id, version))

        if r.status_code == 200:
            return {
                'dates': r.json()['data'],
                'version': version,
            }

    raise RuntimeError('Could not get node dates.')


def get_tunnel_status(ssh_port):
    try:
        output = subprocess.check_output("ssh node{} 'echo OK; exit'".format(ssh_port), shell=True).decode()
        return 'OK' in output
    except:
        return False
