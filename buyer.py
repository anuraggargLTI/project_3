import streamlit as st
import streamlit.components.v1 as stc
from streamlit.components.v1 import html
from streamlit_option_menu import option_menu
import buyer
import seller
import search
import pandas as pd
from pathlib import Path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode,DataReturnMode
#import sqlite3

PAGES = {
    "For Buyers": buyer,
    "For Sellers": seller
}

# html templates
CAR_HTML_TEMPLATE = """
<div style="color:white; width:100%; height:100%; margin:1px; padding:5px; position:sticky; border-radius:1px; border-bottom-right-radius: 1px;
box-shadow:0 0 1px 1px #eee; background-image: url('https://www.hdcarwallpapers.com/thumbs/2023/laferrari_sports_car-t2.jpg'); background-position: center center;
background-size: 280px; width: 225px; height: 175px; background-repeat:no-repeat; border-left: 5px solid #6c6c6c;">
<strong>
<p>{}</p>
<p>{}</p>
<p>{}</p>
<p>{}</p>
</strong>
</div>
"""

CAR_DES_HTML_TEMP = """
<div style='color:#818589'>
{}
<div>"""

# usernames and passwords >>>> HAS TO BE WRITTEN TO ANOTHER FILE EVENTUALLY AND THEN READ IN HERE 
usrs = ['username']
pwrd = ['123456789']

def app():
    st.title('Buyers Please Welcome')
    st.write('Welcome to your Blockchain based car buying platform')
    search.app()

            

    
    # #read to db 
# conn = sqlite3.connect('vehicles.db')
# #vehicles_df = pd.read_csv(Path("./vehicles.csv"), dtype=str)
# vehicles_df = vehicles_df[["id","price","year","model","odometer","cylinders","paint_color","type","state"]]
# vehicles_df.to_sql('vehicles', conn, if_exists='append', index = False)


def app():
    st.title('Buyers Please Welcome')
    st.write('Welcome to your Blockchain based car buying platform')
    search.app()

    car_id = st.number_input('Enter the Car ID to buy:', min_value=0, step=1)
    buy_button = st.button('Buy Car')

    if buy_button:
        if car_id:
            txn_hash = buy_car(car_id)
            st.write(f"Transaction sent! Transaction hash: {txn_hash}")
        else:
            st.error("Please enter a valid Car ID.")

    balance_button = st.button('Check Remaining Balance')
    
    if balance_button:
        balance = get_remaining_balance()
        st.write(f"Your remaining balance: {balance} (in wei)")


import json
from web3 import Web3

# Replace with your Ethereum node URL
eth_node_url = 'https://mainnet.infura.io/v3/INFURA_API_KEY'
w3 = Web3(Web3.HTTPProvider(eth_node_url))

# Replace with your smart contract ABI and address
contract_abi = json.loads [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_tokenAddress",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_currencyTokenAddress",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_carId",
				"type": "uint256"
			}
		],
		"name": "buyCar",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "carCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "cars",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "address payable",
				"name": "seller",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "currencyToken",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getRemainingBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_tokenId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_price",
				"type": "uint256"
			}
		],
		"name": "listCar",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "token",
		"outputs": [
			{
				"internalType": "contract IERC721",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract_address = 'CONTRACT_ADDRESS'

# Replace with your private key and public address
private_key = 'PRIVATE_KEY'
my_address = 'PUBLIC_ADDRESS'

# Set up the contract object
contract = w3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=contract_abi)

# Buy a car using the 'buyCar' function
def buy_car(car_id):
    car = contract.functions.cars(car_id).call()
    car_price = car[2]

    nonce = w3.eth.getTransactionCount(my_address)
    gas_price = w3.eth.gasPrice

    # Replace with the amount of Ether you're willing to pay for gas
    gas_limit = 200000

    transaction = contract.functions.buyCar(car_id).buildTransaction({
        'from': my_address,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
    })

    signed_txn = w3.eth.account.signTransaction(transaction, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return txn_hash.hex()

# Get the remaining balance using the 'getRemainingBalance' function

def get_remaining_balance():
    remaining_balance = contract.functions.getRemainingBalance().call({'from': my_address})
    return remaining_balance
