import os, json


BASE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE_CONFIG = os.path.join(BASE, 'config.json')

try:
    with open(FILE_CONFIG) as config:
        data_json = json.loads(config.read())
except Exception as e:
    print e

status = data_json['status']
STATIC_PATH = data_json['static_path']
GMT = int(data_json['gmt'])
