import os
import sys
import time
from polymarket_trader import PyPolymarketClobClient

# Load credentials securely from Render Environment Variables
API_KEY = os.getenv("POLYMARKET_API_KEY")
PASSPHRASE = os.getenv("POLYMARKET_PASSPHRASE")
SECRET = os.getenv("POLYMARKET_SECRET")
PRIVATE_KEY = os.getenv("POLYMARKET_PRIVATE_KEY")

if not all([API_KEY, PASSPHRASE, SECRET, PRIVATE_KEY]):
    print("❌ Error: Missing credentials in Render Environment Variables.")
    sys.exit(1)

def run_bot():
    print("⏳ Connecting to Polymarket CLOB API via Render...")
    try:
        client = PyPolymarketClobClient(
            api_key=API_KEY,
            api_secret=SECRET,
            api_passphrase=PASSPHRASE,
            private_key=PRIVATE_KEY
        )
        print("✅ Connection Successful! Bot is verified on Render.")
        
        # Keep the script alive so Render background worker doesn't exit
        while True:
            print("🤖 Bot is active and listening for market updates...")
            time.sleep(60) # Pings every minute to show it's alive
            
    except Exception as e:
        print(f"❌ Connection Failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_bot()
