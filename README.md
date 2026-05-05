# Phone Validator Pro API

Phone number validation with carrier, country, line type and format.

**RapidAPI:** https://rapidapi.com/adunaev8419/api/phone-validator-pro1

## Quick Start

```python
import requests

url = "https://phone-validator-pro1.p.rapidapi.com/validate"
headers = {"X-RapidAPI-Key": "YOUR_KEY", "Content-Type": "application/json"}
r = requests.post(url, json={"phone": "+79001234567"}, headers=headers)
print(r.json())
# {"is_valid": true, "country": "Russia", "carrier": "Tele2", "line_type": "MOBILE"}
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /validate | POST | Single phone validation |
| /batch | POST | Batch up to 50 numbers |

## Pricing

| Plan | Price | Requests/hr |
|------|-------|-------------|
| BASIC | Free | 30 |
| PRO | $9.99/mo | 500 |
| ULTRA | $24.99/mo | 5,000 |

See `examples/` for Python, JavaScript, cURL samples.