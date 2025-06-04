import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Error: Command-line argument is not a valid number.")

    api_url = "https://rest.coincap.io/v3/assets/bitcoin"
    api_key = "d8fb1706d13fee235cd03d65f090d1058537fee98816c8b0652a0d0bb0a2be38"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        bitcoin_price_usd = float(data['data']['priceUsd'])
        total_cost_usd = n * bitcoin_price_usd
        formatted_cost = "{:,.4f}".format(total_cost_usd)
        print(f"${formatted_cost}")

    except requests.RequestException as e:
        sys.exit(f"Error: Could not retrieve Bitcoin price. {e}")
    except (KeyError, TypeError) as e:
        sys.exit(f"Error: Invalid API response. {e}")

if __name__ == "__main__":
    main()
