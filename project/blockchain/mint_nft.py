import time
import requests
import json

def send_nft(loan_statement):
    url = "https://api.verbwire.com/v1/nft/mint/mintFromMetadata"

    # Headers and data (use your actual contract address and wallet address)
    headers = {
        "accept": "application/json",
        "X-API-Key": "sk_live_b7624d12-b104-4281-91c2-5dcfdbcdbf98",
        "Content-Type": "application/json"
    }
    data = {
        "quantity": "1",
        "chain": "sepolia",
        "contractAddress": "0xCaedFe8d392A1679a92B755D0F7b5C68fc2aaAe4",
        "data": loan_statement
    }

    # Make the request to mint the NFT
    response = requests.post(url, json=data, headers=headers)
    initial_response = response.json()
    print("Initial response:", initial_response)


    return

send_nft("sup")

url = "https://api.verbwire.com/v1/nft/deploy/deployContract"

# Headers with the Verbwire API key
headers = {
    "accept": "application/json",
    "X-API-Key": "sk_live_b7624d12-b104-4281-91c2-5dcfdbcdbf98", 
    "Content-Type": "application/json"
}

# Data required to deploy the contract
data = {
    "chain": "goerli",  # Specify the blockchain you want to deploy to, e.g., 'sepolia', 'goerli', etc.
    "contractName": "MyNFTCollection",  # Name of your NFT collection
}

# Sending POST request to deploy the contract
response = requests.post(url, json=data, headers=headers)

# Check the response
if response.status_code == 200:
    response_data = response.json()
    print("Contract deployed successfully:")
    print(f"Contract Address: {response_data.get('contractAddress')}")
    print(f"Transaction Hash: {response_data.get('transactionHash')}")
else:
    print("Failed to deploy contract:")
    print(response.text)