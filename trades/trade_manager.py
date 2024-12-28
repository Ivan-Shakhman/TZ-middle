from loguru import logger
import time
import random


class TradeManager:

    def __init__(self, account, proxy, user_agent, web3):
        self.account = account
        self.proxy = proxy
        self.user_agent = user_agent
        self.web3 = web3

    def open_position(self, amount, position_type="long"):
        logger.info(f"Opening {position_type} position for {self.account} with {amount}")

    def close_position(self):
        logger.info(f"Closing position for {self.account}")

    def trade(self, num_transactions, delay_range=(0, 10)):
        for _ in range(num_transactions):
            amount = random.uniform(1, 100)
            self.open_position(amount)
            time.sleep(random.uniform(*delay_range))
            self.close_position()
