import logging
from datetime import datetime
REQUEST_COUNT = 10000

def read_item(number: int):
    return {"number": number+1 }


def run():
    start = datetime.now()
    for i in range(REQUEST_COUNT):
        assert read_item(i)['number'] == i+1
    print(f'{REQUEST_COUNT} requests is completed in {datetime.now() - start}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
