import requests, random, asyncio, string
from telegram import Bot

BOT_TOKEN  = "9275589633:AAFM2_m42_tsosrIlATNk_iJtnEZpX2ZWNk" 
TOKEN_MINT = "7E48NfCy51n3Q2aGZWSoRZmc8CQ1jLu1VB83e9JGpump"
CHAT_ID    = "-1004350295551"

bot = Bot(token=BOT_TOKEN)

# --- GENERATE REAL-LOOKING SOLANA WALLETS ---
def get_fake_wallet():
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=4)) + "..." + "".join(random.choices(chars, k=4))

def get_price(mint):
    try:
        r = requests.get(f"https://api.dexscreener.com/latest/dex/tokens/{mint}").json()
        pair = r["pairs"][0]
        return pair["priceUsd"], pair["volume"]["h24"], pair["priceChange"]["h1"]
    except:
        return None, None, None

async def main():
    print("Stealth Bot starting...")
    while True:
        price, vol, change = get_price(TOKEN_MINT)
        
        # ONLY post price if DexScreener actually has data for the coin!
        if price and price != "0":
            try:
                p_float = float(price)
                if p_float < 0.0001:
                    price_str = f"{p_float:.8f}"
                else:
                    price_str = f"{p_float:.5f}"
                
                msg = await bot.send_message(chat_id=CHAT_ID, text=f"📈 $ILRY Price: ${price_str} | 1h Change: {change}% | Vol: ${vol}")
                await bot.set_message_reaction(chat_id=CHAT_ID, message_id=msg.message_id, reaction="🚀")
            except:
                pass
        
        await asyncio.sleep(random.randint(300, 600))

        # FAKE WHALE (with realistic wallet address)
        if random.random() < 0.6:
            amt = random.randint(150, 4500)
            wall = get_fake_wallet()
            msg = await bot.send_message(chat_id=CHAT_ID, text=f"🐋 WHALE ALERT — {wall} just aped {amt} USD into the pool! Don't fade.")
            try:
                await bot.set_message_reaction(chat_id=CHAT_ID, message_id=msg.message_id, reaction="🔥")
            except:
                pass
        
        await asyncio.sleep(random.randint(600, 1200))

        # HYPE / FAKE REPLIES
        if random.random() < 0.4:
            replies = [
                "Just aped 2 SOL. Let's go 🚀",
                "When CEX listing?",
                "Dev, is liquidity locked?",
                "Chart looks crazy right now. WAGMI.",
                "This is going to 100x easily.",
                "🔥 The community is growing fast.",
                "🤝 Partnership announcement coming very soon. Stay tuned.",
                "💎 If you're fading this, you're going to regret it."
            ]
            await bot.send_message(chat_id=CHAT_ID, text=random.choice(replies))

        print("Cycle complete. Sleeping...")
        # Wait between 20 to 40 minutes
        await asyncio.sleep(random.randint(1200, 2400))

if __name__ == "__main__":
    asyncio.run(main())
