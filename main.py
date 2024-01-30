import requests
from datetime import timezone
import datetime
import time


API_ENDPOINT = "https://api.kraken.com/0/"
def get_order_book(endpoint: str, pair: str, count: int = None):
    if count:
        response = requests.get(f"{endpoint}public/Depth?pair={pair}&count={count}")
    else:
        response = requests.get(f"{endpoint}public/Depth?pair={pair}")

    return response
    

def print_info():
    response = get_order_book(API_ENDPOINT, "BTCUSD")
    time = datetime.datetime.now(timezone.utc).replace(tzinfo=timezone.utc)

    print(response.json())
    print(time) 
    

if __name__ == "__main__":
    while (True):
        print_info()
        time.sleep(300)
