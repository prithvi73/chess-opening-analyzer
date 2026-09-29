import requests

# creating a user agent header before pinging chesscom
headers = {
    "User-Agent" : "ChessOpeningAnalyzer/1.0  (username : prithvi73)"

}

username = "prithvi-in-space"
url = f"https://api.chess.com/pub/player/{username}/games/archives"

# Send the request to API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    archives = data["archives"]
    print(f"Found {len(archives)} months of games!")
    print("First 5 months:", archives[:5])
else:
    print("Error:", response.status_code)

