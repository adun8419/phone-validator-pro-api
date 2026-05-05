const API_KEY = "YOUR_RAPIDAPI_KEY";
const BASE_URL = "https://phone-validator-pro1.p.rapidapi.com";

async function validatePhone(phone) {
  const res = await fetch(`${BASE_URL}/validate`, {
    method: "POST",
    headers: {"X-RapidAPI-Key": API_KEY, "Content-Type": "application/json"},
    body: JSON.stringify({ phone })
  });
  return res.json();
}

validatePhone("+79001234567").then(console.log);