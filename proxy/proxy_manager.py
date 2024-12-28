import random


class ProxyManager:

    def __init__(self, proxy_file, proxy_type: str = "residential") -> None:

        with open(proxy_file, "r") as f:
            self.proxies = [line.strip() for line in f.readlines()]

        self.proxy_type = proxy_type

    def get_proxy(self):
        if self.proxy_type == "mobile":
            proxy = random.choice(self.proxies)
            return proxy.split("|")[0], proxy.split("|")[1]
        return random.choice(self.proxies)

