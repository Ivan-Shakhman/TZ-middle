from concurrent.futures import ThreadPoolExecutor
from accounts.account_manager import AccountManager
from proxy.proxy_manager import ProxyManager
from trades.trade_manager import TradeManager
from settings import SETTINGS

if __name__ == "__main__":
    accounts = AccountManager("accounts.txt")
    proxies = ProxyManager("proxies.txt")

    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(SETTINGS["max_threads"]):
            account = accounts.get_account()
            proxy = proxies.get_proxy()
            executor.submit(TradeManager(account, proxy).trade, 10)
