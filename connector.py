import streamlit as st
from ml_model.ml_model import ml_function
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from web3 import Web3
import os
import json
from dotenv import load_dotenv
import numpy as np
import streamlit as st

#st.title('Sellers Please Welcome')
#st.write('Welcome your blockchain based car buying platform')


load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache_resource()
# Define the load_contract function
# Set the contract address (this is the address of the deployed contract)


def load_contract():

    # Load Art Gallery ABI
    with open(Path('./contracts/compiled/contract_abi.json')) as f:
        contract_abi = json.load(f)


    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("BUYER_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    # Return the contract from the function
    return contract


# Load the contract
contract = load_contract()




################################################################################
# Award Certificate
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
#student_account = st.selectbox("Select Account", options=accounts)

#if st.button("Get Balance"):
    
  #  st.write(balance_wei)
    # Convert the balance from Wei to Ether
   # balance_eth = w3.fromWei(balance_wei, 'ether')
  #  st.write(f"Ether balance for {student_account}: {balance_eth}")
private_key = '0xd67abb212b5ac17be94408dbdfc55b729310976df20480b38add7f3f61a7a623'
def return_balance():
   # balance_wei = contract.functions.getEtherBalance(account).call()
    balance_wei = w3.eth.getBalance(os.getenv("USER_ADDRESS"))
    balance_eth = w3.fromWei(balance_wei, 'ether')
    return balance_eth
#def buy_car(car_id):
#    contract_address = os.getenv("BUYER_CONTRACT_ADDRESS")
#    car = contract.functions.cars(car_id).call()
#    car_price = car[2]

#    nonce = w3.eth.getTransactionCount(contract_address)
#    gas_price = w3.eth.gasPrice

    # Replace with the amount of Ether you're willing to pay for gas
#    gas_limit = 200000

   # transaction = contract.functions.buyCar(car_id,price).buildTransaction({
   #     'from': contract_address,
   #     'gas': gas_limit,
   #     'gasPrice': gas_price,
   #     'nonce': nonce,
   # })

    #signed_txn = w3.eth.account.signTransaction(transaction, private_key)
    #txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    #return txn_hash.hex()
# Get the remaining balance using the 'getRemainingBalance' function
def get_remaining_balance():
    contract_address = os.getenv("BUYER_CONTRACT_ADDRESS")
    remaining_balance = contract.functions.getRemainingBalance().call({'from': contract_address})
    return remaining_balance


def buy_car2(value):
    sender = os.getenv("USER_ADDRESS")
    # Set the receiver address
    receiver = os.getenv("THIRD_PARTY_ADDRESS")
    # Set units of gas
    gas = 21000
    # Convert balance from ether to wei
    value = w3.toWei(value, 'ether')
    # Send the transaction to the blockchain
    w3.eth.send_transaction({'to': receiver , 'from': sender , "gas": gas, "value": value})

def sell_car(value):
    receiver = os.getenv("USER_ADDRESS")
    # Set the receiver address
    sender = os.getenv("THIRD_PARTY_ADDRESS")
    # Set units of gas
    gas = 21000
    # Convert balance from ether to wei
    value = w3.toWei(value, 'ether')
    # Send the transaction to the blockchain
    w3.eth.send_transaction({'to': receiver , 'from': sender , "gas": gas, "value": value})