import logging
import requests
from datetime import datetime
REQUEST_COUNT = 10000


def run():
    start = datetime.now()
    for i in range(REQUEST_COUNT):
        resp = requests.get(f'http://localhost:8000/increase/{i}')
        assert resp.json()['number'] == i+1
    print(f'{REQUEST_COUNT} requests is completed in {datetime.now() - start}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
