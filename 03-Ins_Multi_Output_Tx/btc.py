from bit import wif_to_key

key = wif_to_key("92jGVAFiSNJQdJH21qJYBzH9bsJMZ1Q6GiHqS1QNY6edh6Rn36g")

balance = key.get_balance("btc")

print(balance)
