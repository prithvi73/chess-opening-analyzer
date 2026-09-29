import pandas as pd
import requests

# creating a user agent header before pinging chesscom
headers = {
    "User-Agent" : "ChessOpeningAnalyzer/1.0  (username : prithvi73)"

}

username = "prithvi-in-space"
# getting only games from April 2026
url = f"https://api.chess.com/pub/player/{username}/games/2026/04"

# Send the request to API
response = requests.get(url, headers=headers)

# Response Code 200 = Request Succesful
if response.status_code == 200:
    data = response.json()

    df = pd.json_normalize(data["games"])

    print("--- EVERY AVAILABLE COLUMN ---")
    # This prints out a clean list of every column name we have to work with
    print(df.columns.tolist())
    
    print("\n--- SNEAK PEEK AT THE PGN COLUMN ---")
    # The PGN column contains the actual moves and opening data
    print(df["pgn"].iloc[0])

else:
    print("Error:", response.status_code)

