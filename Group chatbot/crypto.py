#DELIVERABLE 1
def crypto_advisor():
    # Predefined crypto dataset
    crypto_db = {
        "Bitcoin": {
            "price_trend": "rising",
            "market_cap": "high",
            "energy_use": "high",
            "sustainability_score": 3/10
        },
        "Ethereum": {
            "price_trend": "stable",
            "market_cap": "high",
            "energy_use": "medium",
            "sustainability_score": 6/10
        },
        "Cardano": {
            "price_trend": "rising",
            "market_cap": "medium",
            "energy_use": "low",
            "sustainability_score": 8/10
        }
    }

    # Welcome message (friendly tone)
    print("\nWelcome to CryptoAdvisor! 👋")
    print("I can help you find cryptocurrencies based on profitability and sustainability.")
    print("Type 'help' for options or 'exit' to quit.\n")

   # DELIVERABLE 2

def get_eco_friendly_crypto():
    cryptos = {
        "Ethereum": "Transitioned to Proof of Stake, reducing energy consumption.",
        "Cardano": "PoS-based with a strong focus on sustainability.",
        "Algorand": "Carbon-negative blockchain.",
        "Tezos": "Energy-efficient PoS protocol.",
        "Chia": "Uses Proof of Space and Time instead of mining."
    }

    return cryptos

eco_friendly_options = get_eco_friendly_crypto()
print("Most sustainable cryptocurrencies:")
for name, description in eco_friendly_options.items():
    print(f"- {name}: {description}")


# deliverable 3 and 4

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",      # Current price trend
        "market_cap": "high",         # Market capitalization
        "energy_use": "high",         # Energy consumption
        "sustainability_score": 3/10  # Sustainability score (out of 10)
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Returns a list of cryptos that are currently trending up
def get_trending_crypto():
    trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
    return trending

# Returns the crypto with the highest sustainability score
def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

# Returns a crypto that is both rising and has a high market cap
def get_profitable():
    for name, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            return name
    return None

# Main chatbot function that interacts with the user
def chatbot():
    print("Hi! I'm CryptoBuddy 🤖. Ask me about trending or sustainable cryptocurrencies!")
    while True:
        user_query = input("You: ").lower()  # Get user input and convert to lowercase
        # Check for trending crypto queries
        if "trending" in user_query or "up" in user_query:
            trending = get_trending_crypto()
            print(f"CryptoBuddy: Trending cryptos: {', '.join(trending)} 🚀")
        # Check for sustainability queries
        elif "sustainable" in user_query or "eco" in user_query:
            recommend = get_most_sustainable()
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
        # Check for profitability queries
        elif "profit" in user_query or "best" in user_query:
            recommend = get_profitable()
            if recommend:
                print(f"CryptoBuddy: {recommend} is rising and has a high market cap!")
            else:
                print("CryptoBuddy: No highly profitable crypto found right now.")
        # Exit the chatbot
        elif "exit" in user_query or "quit" in user_query:
            print("CryptoBuddy: Remember, crypto is risky—always do your own research! Bye! 👋")
            break
        # Handle unrecognized queries
        else:
            print("CryptoBuddy: Sorry, I didn't understand. Try asking about trending, sustainable, or profitable cryptos.")

# Run the chatbot if this file is executed directly
if __name__ == "__main__":
    chatbot()



# Sample Queries

# Trending Crypto Queries
# Which crypto is trending up?
# What coins are trending?
# Show me trending cryptos.
# Which cryptocurrencies are going up?
# Sustainability Queries
# What’s the most sustainable coin?
# Which crypto is eco-friendly?
# Recommend a sustainable cryptocurrency.
# Which coin is best for the environment?
# Profitability Queries
# Which crypto is most profitable?
# What is the best coin to invest in?
# Which crypto has the best profit?
# Recommend a profitable cryptocurrency.
# Exit Queries
# exit
# quit
# Unrecognized Query Example
# Tell me a joke.
# Who created Bitcoin?