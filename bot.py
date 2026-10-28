import requests, time, random
from telegram import Bot

# --- YOUR INFO ---
BOT_TOKEN  = "9275589633:AAFM2_m42_tsosrIlATNk_iJtnEZpX2ZWNk" 
TOKEN_MINT = "7E48NfCy51n3Q2aGZWSoRZmc8CQ1jLu1VB83e9JGpump"
CHAT_ID    = "-1004350295551"

bot = Bot(token=BOT_TOKEN)

# --- THE FAKE DATA ---
wallets = ["7x9a…f2c", "3k2b…e8d", "9m4f…a1b", "2c8z…p4m", "5t1r…w9z"]
hype_messages = [
    "🔥 The community is growing fast. Over 500 new holders in the last hour!",
    "🚀 $ILRY is trending on DexScreener. The dev team is based.",
    "🤝 Partnership announcement coming very soon. Stay tuned.",
    "💎 If you're fading this, you're going to regret it. Chart is beautiful.",
    "📢 Audit is officially complete. Contract renounced. We are SAFU."
]

def get_price(mint):
    try:
        r = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{mint}").json()
        pair = r["pairs"][0]
        return pair["priceUsd"], pair["volume"]["h24"]
    except:
        return "0.00001", "0"

print("Bot is starting...")

while True:
    price, vol = get_price(TOKEN_MINT)
    
    # 1. Post Price Update
    bot.send_message(chat_id=CHAT_ID, text=f"📈 $ILRY Price: ${price} | 24h Vol: ${vol}")
    time.sleep(5) # wait 5 seconds between messages
    
    # 2. Fake Whale Alert (80% chance every loop)
    if random.random() < 0.8:
        amt = random.randint(1000, 15000)
        wall = random.choice(wallets)
        bot.send_message(chat_id=CHAT_ID, text=f"🐋 WHALE ALERT — {wall} just aped {amt} USD into the pool! Don't fade.")
    time.sleep(10)
    
    # 3. Hype Message (Picks a random one from the list)
    if random.random() < 0.5:
        hype = random.choice(hype_messages)
        bot.send_message(chat_id=CHAT_ID, text=hype)
    time.sleep(10)

    # 4. FOMO Countdown
    if random.random() < 0.4:
        pct = random.randint(5, 15)
        bot.send_message(chat_id=CHAT_ID, text=f"⏳ FOMO ALERT: Only {pct}% of the supply is left before the next price milestone. Buy now before it's too late.")
    time.sleep(10)

    print("Cycle complete. Sleeping for 30 minutes...")
    time.sleep(1800) # Wait 30 minutes before doing the whole cycle again
