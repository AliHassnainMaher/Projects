import requests

# Function to fetch the latest exchange rates
def fetch_exchange_rates():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('rates', {})
    else:
        return {}

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code"
    
    # Convert amount to USD first
    amount_in_usd = amount / exchange_rates[from_currency]
    
    # Convert from USD to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount

def main():
    # Fetch the latest exchange rates
    exchange_rates = fetch_exchange_rates()

    # Example usage
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency code to convert from (e.g., USD, INR): ").upper()
    to_currency = input("Enter the currency code to convert to (e.g., USD, INR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
