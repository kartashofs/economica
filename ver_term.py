from random import randint

bots, players, month = 2, [], 0

class Players:
    amount = 0

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

offers = [0 for x in range((Players.amount + 1))]
sell_offers = [0 for x in range((Players.amount + 1))]
investment = [{'month': 0, 'got': 0} for x in range((Players.amount + 1))]
buildings = [[{'remaining': 0, 'type': 0} for i in range((Players.amount + 1))] for x in range((Players.amount + 1))]
global fucking_bots
fucking_bots = players[1]
def payments(player):
    for fucking_bot in fucking_bots:
        fucking_bot.cash -= (fucking_bot.esm * 300 + fucking_bot.egp * 500 + fucking_bot.fab * 1000 + 1500 * fucking_bot.autofab)

def bank(instances):
    global current_rate
    if month != 1: current_rate = bank_instances[randint(1, 4)]
    else: current_rate = bank_instances[3]


def bot_processing(players):
    global current_esm, current_min, budget
    current_esm = current_rate.get('ECM')
    current_min = current_rate.get('min_price')
    for fucking_bot in fucking_bots:
        if fucking_bot.cash > current_rate.get('min_price') + 200: 
            budget = randint(current_min - 200, current_min + 200)
            offers[fucking_bots.index(fucking_bot)] = budget
        else:
            offers[fucking_bots.index(fucking_bot)] = 0

def get_bank_choice(offers):
    global encounter
    encounter = 1
    offers = [0 for x in range((Players.amount + 1))]
    for x in offers:
        if x >= current_min:
            fucking_bots[encounter].cash -= current_esm * x
            fucking_bots[encounter].esm += current_esm
        encounter += 1

def production(players):
    for fucking_bot in fucking_bots[1:]:
        if fucking_bot.ECM >= 1:
            if fucking_bot.autofab == 0:
                while fucking_bot.cash > 3500:
                    fucking_bot.cash -= 2000
                    fucking_bot.ecm -= 1
                    fucking_bot.egp += 1
            else:
                while fucking_bot.cash > 3500:
                    fucking_bot.cash -= 3000
                    fucking_bot.ecm -= 2
                    fucking_bot.egp += 2

def sellebration(players):
    global current_egp, current_max, budget
    current_egp = current_rate.get('EGP')
    current_max = current_rate.get('max_price')
    for fucking_bot in fucking_bots[1:]:
        if fucking_bot.egp >= 1: 
            budget = randint(current_max - 1500, current_max + 1500)
            sell_offers[fucking_bots.index(fucking_bot)] = budget
        else:
            sell_offers[fucking_bots.index(fucking_bot)] = 0

def gang_bank_choice(sell_offers, players):
    global encounter
    encounter = 0
    for x in sell_offers:
        if x != 0 and x <= current_max:
            players[encounter].cash += current_egp * x
            if players[encounter].egp >= current_egp: players[encounter].egp -= current_egp
            else: players[encounter].egp = 0
            encounter += 1

def be_invested(players):
    encounter = 1
    for fucking_bot in fucking_bots[1:]:
        if fucking_bot.cash <= 1500:
            investment_amount = fucking_bot.fab * 5000 + fucking_bot.autofab * 10000
            investment[encounter].update(month=month, got=investment_amount)
            fucking_bot.cash += investment_amount

def build_factories(players):
    for fucking_bot in fucking_bots[1:]:
        if fucking_bot.cash - 7000 > 3500:
            for i in buildings[fucking_bot]:
                for o in i:
                    if o.get('remaining') == 0:
                        o.update(remaining=9, type=2)
        if fucking_bot.cash - 5000 > 3500:
            for i in buildings[fucking_bot]:
                for o in i:
                    if o.get('remaining') == 0:
                        o.update(remaining=5, type=1)

while month <= 12:
    month += 1
    payments(players)
    bank(bank_instances)
    bot_processing(players)
    get_bank_choice(offers)
    production(players)
    sellebration(players)
    gang_bank_choice(sell_offers, players)
    be_invested(players)
    build_factories(players)

