from random import randint

bots, players, month = 2, [], 0

class Players:
    amount = bots

    def __init__(self, fab, autofab, esm, egp, cash):  
        self.fab = fab
        self.autofab = autofab
        self.esm = esm
        self.egp = egp
        self.cash = cash
        Players.amount += 1 

players = [Players(2, 0, 4, 2, 10000), [Players(2, 0, 4, 2, 10000) for x in range(Players.amount)]]
bank_instances = [{'ECM': 1.0, 'min_price': 800, 'EGP': 3.0, 'max_price': 6500},
{'ECM': 1.5, 'min_price': 650, 'EGP': 2.5, 'max_price': 6000},
{'ECM': 2.0, 'min_price': 500, 'EGP': 2.0, 'max_price': 5500},
{'ECM': 2.5, 'min_price': 400, 'EGP': 1.5, 'max_price': 5000},
{'ECM': 3.0, 'min_price': 300, 'EGP': 1.0, 'max_price': 4500}
]

offers = [(Players.amount + 1) * 0]

def payments(player):
    for x in players:
        x.cash -= (x.esm * 300 + x.egp * 500 + x.fab * 1000 + 1500 * x.autofab)

def bank(instances):
    global current_rate
    if month != 0: current_rate = bank_instances[randint(1, 5)]
    else: current_rate = bank_instances[3]


def bot_processing(players):
    global current_esm, current_min, budget
    current_esm = current_rate.get('ECM')
    current_min = current_rate.get('min_price')
    for x in players[1:]:
        if x.cash > current_rate.get('min_price') + 200: 
            budget = randint(current_min - 200, current_min + 200)
            offers.append(budget)

def get_bank_choice(offers):
    for x in offers:
        if x >= current_min:
            x.cash -= current_esm * x
            x.esm += current_esm