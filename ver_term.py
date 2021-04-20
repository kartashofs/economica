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
sell_offers = [(Players.amount + 1) * 0]
investment = [(Players.amount + 1) * {'month': 0, 'got': 0}]
buildings = [(Players.amount + 1) * [6 * {'remaining': 0, 'type': 0}]]

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

def production(players):
    for x in players[1:]:
        if x.ECM >= 1:
            if x.autofab == 0:
                while x.cash > 3500:
                    x.cash -= 2000
                    x.ecm -= 1
                    x.egp += 1
            else:
                while x.cash > 3500:
                    x.cash -= 3000
                    x.ecm -= 2
                    x.egp += 2

def sellebration(players):
    global current_egp, current_max, budget
    current_egp = current_rate.get('EGP')
    current_max = current_rate.get('max_price')
    for x in players[1:]:
        if x.egp >= 1: 
            budget = randint(current_max - 1500, current_max + 1500)
            sell_offers.append(budget)

def gang_bank_choice(offers, players):
    global encounter
    encounter = 0
    for x in offers:
        if x != 0 and x <= current_max:
            players[encounter].cash += current_egp * x
            if players[encounter].egp >= current_egp: players[encounter].egp -= current_egp
            else: players[encounter].egp = 0
            encounter += 1

def be_invested(players):
    encounter = 1
    for x in players[1:]:
        if x.cash <= 1500:
            investment_amount = x.fab * 5000 + x.autofab * 10000
            investment[encounter].update(month=month, got=investment_amount)
            x.cash += investment_amount

def build_factories(players):
    for x in players[1:]:
        if x.cash - 7000 > 3500:
            for i in buildings[x]:
                for o in i:
                    if o.get('remaining') == 0:
                        o.update(remaining=9, type=2)
        if x.cash - 5000 > 3500:
            for i in buildings[x]:
                for o in i:
                    if o.get('remaining') == 0:
                        o.update(remaining=5, type=1)
