from bit import wif_to_key

key = wif_to_key("92jGVAFiSNJQdJH21qJYBzH9bsJMZ1Q6GiHqS1QNY6edh6Rn36g")

action = "display_transaction_information"

if action == "send_to_multiple_outputs":
    # replace with different addresses
    addresses = [
        "mnwreGmyhjSUmNDoyBnuFW4saehF5mgYPa",
        "mzvfGntAHhGSXVChRhCyVEe3FDrG8ZEgKh",
    ]

    outputs = []

    for address in addresses:
        outputs.append((address, 0.000001, "btc"))

    print(key.send(outputs))

elif action == "display_transaction_information":

    usd = key.balance_as("usd")
    hist = key.get_transactions()
    uxto = key.get_unspents()

    print(usd)
    print(hist)
    print(uxto)

