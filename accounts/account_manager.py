import random


class AccountManager:
    def __init__(self, accounts_file) -> None:
        with open(accounts_file, "r") as f:
            self.accounts = [line.strip() for line in f.readlines()]

    def randomize(self):
        random.shuffle(self.accounts)

    def get_account(self):
        if self.accounts:
            return self.accounts.pop(0)
        print("No accounts available!")
