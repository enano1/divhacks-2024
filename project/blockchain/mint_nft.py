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
        "chain": "polygon",
        "contractAddress": "0x4C293079F021FF1e4DeBA6396a9C2D22D3068B61",
        "recipientAddress": "0xd33dE88B94a56544034bc8c829078eba5DbF68f8",
        "data": loan_statement
    }

    # Make the request to mint the NFT
    response = requests.post(url, json=data, headers=headers)
    initial_response = response.json()
    print("Initial response:", initial_response)


    return

# url = "https://api.verbwire.com/v1/nft/deploy/deployContract"

# # Headers with the Verbwire API key
# headers = {
#     "accept": "application/json",
#     "X-API-Key": "sk_live_b7624d12-b104-4281-91c2-5dcfdbcdbf98", 
#     "Content-Type": "application/json"
# }

# # Data required to deploy the contract
# data = {
#     "chain": "polygon",  # Specify the blockchain you want to deploy to, e.g., 'sepolia', 'goerli', etc.
#     "contractName": "MyNFTCollection",  # Name of your NFT collection
# }

# # Sending POST request to deploy the contract
# response = requests.post(url, json=data, headers=headers)

# # Check the response
# if response.status_code == 200:
#     response_data = response.json()
#     print("Contract deployed successfully:")
#     print(f"Contract Address: {response_data.get('contractAddress')}")
#     print(f"Transaction Hash: {response_data.get('transactionHash')}")
# else:
#     print("Failed to deploy contract:")
#     print(response.text)