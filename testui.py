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

st.title('Sellers Please Welcome')
st.write('Welcome your blockchain based car buying platform')


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
student_account = st.selectbox("Select Account", options=accounts)

if st.button("Get Balance"):
    balance_wei = contract.functions.getEtherBalance(student_account).call()
    st.write(balance_wei)
    # Convert the balance from Wei to Ether
#    balance_eth = w3.fromWei(balance_wei, 'ether')
#    st.write(f"Ether balance for {student_account}: {balance_eth}")



