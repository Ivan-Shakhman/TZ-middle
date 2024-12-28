import random


PLATFORMS = [
    "Windows NT 10.0; Win64; x64",
    "Macintosh; Intel Mac OS X 10_15_7",
    "X11; Linux x86_64",
    "Windows NT 6.1; Win64; x64",
    "Windows NT 10.0; ARM64",
    "Macintosh; Intel Mac OS X 12_6",
    "X11; Ubuntu; Linux x86_64",
    "Android 11; Mobile; rv:90.0",
    "iPhone; CPU iPhone OS 15_5 like Mac OS X",
]

BROWSERS = [
    "Mozilla/5.0",
    "AppleWebKit/537.36 (KHTML, like Gecko)",
    "Chrome/105.0.5195.125",
    "Safari/537.36",
    "Edge/18.18363",
    "Firefox/90.0",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.12.388 Version/12.14",
]


def get_random_user_agents(count_of_agents):
    user_agents = []
    for _ in range(int(count_of_agents)):
        platform = random.choice(PLATFORMS)
        browser = " ".join(random.sample(BROWSERS, random.randint(2, 4)))
        user_agent = f"{random.choice(BROWSERS)} ({platform}) {browser}"
        user_agents.append(user_agent)

    return user_agents
