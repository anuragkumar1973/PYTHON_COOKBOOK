import requests
# Get latest exchange rates
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
data = response.json()
print("EUR to USD rate:", data['rates']['EUR'])
print("\n INR to USD rate:", data['rates']['INR'])