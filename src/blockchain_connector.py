# blockchain_connector.py

from web3 import Web3
import requests

class BlockchainConnector:
    def __init__(self):
        # Replace with your actual RPC URLs or Infura endpoints
        self.ethereum_rpc_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
        self.bitcoin_api_url = "https://blockstream.info/api"

        self.web3 = Web3(Web3.HTTPProvider(self.ethereum_rpc_url))

    def is_ethereum_connected(self):
        return self.web3.is_connected()

    def get_eth_balance(self, address):
        try:
            balance_wei = self.web3.eth.get_balance(address)
            balance_eth = self.web3.from_wei(balance_wei, 'ether')
            return float(balance_eth)
        except Exception as e:
            print(f"Error fetching Ethereum balance: {e}")
            return None

    def get_btc_balance(self, address):
        try:
            url = f"{self.bitcoin_api_url}/address/{address}"
            response = requests.get(url)
            data = response.json()
            confirmed = data.get("chain_stats", {}).get("funded_txo_sum", 0)
            spent = data.get("chain_stats", {}).get("spent_txo_sum", 0)
            balance_sats = confirmed - spent
            return balance_sats / 1e8
        except Exception as e:
            print(f"Error fetching Bitcoin balance: {e}")
            return None

    def send_eth_transaction(self, from_address, private_key, to_address, amount_eth, gas=21000, gas_price_gwei=50):
        try:
            nonce = self.web3.eth.get_transaction_count(from_address)
            tx = {
                'nonce': nonce,
                'to': to_address,
                'value': self.web3.to_wei(amount_eth, 'ether'),
                'gas': gas,
                'gasPrice': self.web3.to_wei(gas_price_gwei, 'gwei')
            }

            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.to_hex(tx_hash)
        except Exception as e:
            print(f"Error sending ETH transaction: {e}")
            return None

    def check_eth_transaction(self, tx_hash):
        try:
            tx_receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            return tx_receipt
        except Exception as e:
            print(f"Error checking transaction: {e}")
            return None
