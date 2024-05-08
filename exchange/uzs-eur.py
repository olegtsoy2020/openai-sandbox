import requests
import json
import time
from functools import lru_cache

API_URL = 'https://api.exchangerate-api.com/v4/latest/EUR'
API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your API key
CACHE_TIMEOUT = 3600  # Cache exchange rate for 1 hour

@lru_cache(maxsize=1)
def get_exchange_rate():
    try:
        response = requests.get(API_URL, params={'key': API_KEY})
        response.raise_for_status()
        data = json.loads(response.text)
        uzs_to_eur_rate = data['rates']['UZS']
        return uzs_to_eur_rate
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def convert_uzs_to_eur(uzs_amount, exchange_rate):
    if exchange_rate is None:
        return None
    eur_amount = uzs_amount / exchange_rate
    return eur_amount

def main():
    while True:
        exchange_rate = get_exchange_rate()
        if exchange_rate is None:
            print("Failed to retrieve exchange rate. Try again later.")
            break
        print(f"Today's exchange rate: 1 UZS = {exchange_rate:.2f} EUR")
        
        while True:
            try:
                uzs_amount = float(input("Enter UZS amount to convert: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        eur_amount = convert_uzs_to_eur(uzs_amount, exchange_rate)
        print(f"{uzs_amount} UZS = {eur_amount:.2f} EUR")
        time.sleep(1)  # Wait for 1 second before asking for input again

if __name__ == "__main__":
    main()
