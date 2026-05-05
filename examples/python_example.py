import requests

# Phone Validator Pro
# Free API key: https://rapidapi.com/adunaev8419/api/phone-validator-pro1

API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://phone-validator-pro1.p.rapidapi.com"
headers = {"X-RapidAPI-Key": API_KEY, "Content-Type": "application/json"}

def validate_phone(phone, country_code=None):
    payload = {"phone": phone}
    if country_code:
        payload["country_code"] = country_code
    r = requests.post(f"{BASE_URL}/validate", json=payload, headers=headers)
    return r.json()

def validate_batch(phones):
    r = requests.post(f"{BASE_URL}/batch", json={"phones": phones}, headers=headers)
    return r.json()

if __name__ == "__main__":
    print(validate_phone("+79001234567", "RU"))
    print(validate_batch([{"phone": "+79001234567"}, {"phone": "+447911123456"}]))