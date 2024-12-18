import json
import requests

# Make the request to the API
responses = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

# Use the .json() method to parse the response directly
data = responses.json()

# Print the data
print(data)
print(responses.text) 