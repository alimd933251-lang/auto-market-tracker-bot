import requests
from datetime import datetime

def check_market():
    print(f"=== MARKET TRACKER RUN ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC) ===")
    
    # Track Crypto (Bitcoin) - 100% Free Public API
    try:
        btc_res = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
            timeout=10
        ).json()
        print(f"Bitcoin: ${btc_res['bitcoin']['usd']:,} USD")
    except Exception as e:
        print(f"Bitcoin fetch failed: {e}")

    # Track Currency Rates (USD to INR) - 100% Free Public API
    try:
        forex_res = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10).json()
        print(f"USD to INR: ₹{forex_res['rates']['INR']:.2f}")
    except Exception as e:
        print(f"Forex fetch failed: {e}")
        
    print("==================================================")

if __name__ == "__main__":
    check_market()
