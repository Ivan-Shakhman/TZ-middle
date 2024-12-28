from datetime import datetime


def log_transaction(account, position, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"logs/{account}_transactions.log", "a") as f:
        f.write(f"{timestamp} - {position} - {amount}\n")
