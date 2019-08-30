blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction = [1]):
    blockchain.append([last_transaction,transaction_amount])
    

def user_input():
    tx_amount = float(input('Your transaction amount:'))
    return tx_amount

add_value(user_input())
add_value(user_input() , get_last_blockchain_value())
add_value(user_input() , get_last_blockchain_value())

print(blockchain) 