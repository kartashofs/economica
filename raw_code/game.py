from tkinter import *
from random import randint
import threading
import time
  
players = []
month = 0
flag = False
y = 0
global loT
loT = 0
global sending
sending = 0
global credit_value
credit_value = 0
global build_value
build_value = 0
buildings = []
sell_offers = []
fucking_bots = []
global cost_egp, counting_egp
cost_egp, counting_egp = 0, 0

class Players:
    amount = 0
    def __init__(self, fab, autofab, esm, egp, cash):  
        self.fab = fab
        self.autofab = autofab
        self.esm = esm
        self.egp = egp
        self.cash = cash
        Players.amount += 1
        
    
def payments(players, fucking_bots,buildings, investment):
    bot, count = 0, 1
    global month
    cntt = month+1
    month = cntt
    if month != 1:
        current_min = current_rate.get('min_price')
        current_max = current_rate.get('max_price')
    else:
        current_min = 400
        current_max = 5000
    print(month)
    use = ''
    banking.destroy()
    print('Был произведен пересчет постоянных издержек. \nПроизошло списание: \n')
    players[0].cash -= (players[0].esm * 300 + players[0].egp * 500 + players[0].fab * 1000 + 1500 * players[0].autofab)
    print('Игрок: ' + names[0] +' ,Баланс: ' + str(players[0].cash) )
    
    for fucking_bot in fucking_bots:
        fucking_bot.cash -= (fucking_bot.esm * 300 + fucking_bot.egp * 500 + fucking_bot.fab * 1000 + 1500 * fucking_bot.autofab)
        print('Игрок: ' + names[count] + ' ,Баланс: ' + str(fucking_bot.cash))
        bot += 1
        count += 1
    if month != 1:
        for i in buildings[0]:
            if i.get('remaining') != 0 and i.get('type') != 0:
                i.update(remaining=i.get('remaining')-1, type=i.get('type'))
                if i.get('remaining') == 0 and i.get('type') != 0:
                    if i.get('type') == 1:
                        players[0].fab += 1
                        use = 'Обычная фабрика'
                    elif i.get('type') == 2:
                        players[0].autofab += 1
                        use = 'Автоматизированная фабрика'
        counter = 1
        for fucking_bot in fucking_bots:
            for i in buildings[counter]:
                if i.get('remaining') != 0 and i.get('type') != 0:
                    i.update(remaining=i.get('remaining')-1, type=i.get('type'))
                    if i.get('remaining') == 0 and i.get('type') != 0:
                        if i.get('type') == 1:
                            fucking_bot.fab += 1
                        else:
                            fucking_bot.autofab += 1
            counter += 1
    if use == '':
        s = 'Месяц: ' + str(month) + '  Ваш баланс: ' + str(players[0].cash) + '\nесм: ' + str(players[0].esm)+ '\nегп: ' + str(players[0].egp)
    elif use == 'Обычная фабрика':
        s = 'Месяц: ' + str(month) + '  Ваш баланс: ' + str(players[0].cash) + ' Вам доступна новая обычная фабрика'
    elif use == 'Автоматизированная фабрика':
        s = 'Месяц: ' + str(month) + '  Ваш баланс: ' + str(players[0].cash) + ' Вам доступна новая автоматизированная фабрика'        
    money1.configure(text=s)
    money1.grid(column=0, row=0)
    global flag
    flag = False
    s1 = ''
    cnt = 1
    enc = 0
    res = 0
    for bot in fucking_bots:
        amount = 0
        if bot.cash < 0:
            s1 += names[cnt] + ' обанкротился\n'
            flag = True
        else:
            amount = investment[cnt].get("got")
            res = bot.cash + (bot.esm * current_min) + (bot.egp * current_max) - amount
            s1 += 'Капитал ' + names[cnt]+ ':'  + str(res)+ '$' + '\n'
        cnt += 1
    
    if players[0].cash > 0:
        res = 0
        amount = int(investment[0].get("got"))
        res = players[0].cash + (players[0].esm * current_min) + (players[0].egp * current_max) - amount
        s1 += 'Капитал ' +  names[0] + ':' + str(res) + '$'
        bankrot.configure(text=s1)
    else:
        s1 += names[0] + ' обанкротился'
        flag = True
        bankrot.configure(text=s1)
            
        
        
            
    
def pay():
    apl_inf.destroy()
    banking.destroy()
    global bankrot
    bankrot = Label(text="")
    global money1
    money1 = Label(window, text="")
    payments(players, fucking_bots,buildings, investment)
    global information
    if flag:
        bankrot.grid(column=0, row=1)
    else:
        information = Button(text="Next", command=listT)
        information.grid(column=0, row=1)
        print(month, 'мес')
    print('Flag= ',flag)
    

    
    

def bank(instances): 
    global current_rate
    if month != 1: current_rate = bank_instances[randint(1, 4)]
    else: current_rate = bank_instances[3]
    print(current_rate, '\n')
    #texting = Label(window,text=current_rate)
    #texting.grid(column=0, row=1)
    #current_min = current_rate.get('min_price')
    #print(current_min)
    print(month)
    

def listT():
    money1.destroy()
    information.destroy()
    bank(bank_instances)
    global player_cash 
    player_cash = Button(text="Предложить банку цену\n для покупки есм", command=lot)
    player_cash.grid(column=0, row=1)
    
def bot_processing(fucking_bots, players, loT, bots):
    print(bots, 'Боты')
    global current_esm, current_min, budget
    current_esm = current_rate.get('ECM')
    current_min = current_rate.get('min_price')
    #offers = [0 for x in range((bots + 1))]
    offers[0] = loT
    print(offers, 'ОФФЕРСЫ')
    enc = 1
    for fucking_bot in fucking_bots:
        if fucking_bot.cash > current_min + 500: 
            budget = randint(current_min - 300, current_min +200)
            offers[enc] = budget            
        else:
            offers[enc] = 0
        enc += 1
        
    cnt = 0

    for x in offers:
        print(x, names[cnt])
        cnt += 1
    #print(current_min)
    print(offers, 'офферс')
    
def lot():
    player_cash.destroy()
    global player_lot, lot_done
    player_lot = Entry(window, width=10)
    lot_done = Button(text="Предложить цену", command=lot_next)
    player_lot.grid(column=0, row=0)
    lot_done.grid(column=1, row=0)

def lot_next():
    loT = int(player_lot.get())
    player_lot.destroy()
    lot_done.destroy()
    global lot_condition
    lot_condition = Button(text="Узнать состояние транзакции", command=get_bank)
    bot_processing(fucking_bots, players, loT, bots)
    lot_condition.grid(column=0, row=0)
    
def get_bank_choice(offers, fucking_bots, players, current_rate):
    print(offers, "OFFERS")
    encounter = 0
    cnt = 1
    current_min = current_rate.get('min_price')
    current_esm = current_rate.get('ECM')
    for x in offers[1:]:
        if x >= current_min:
            fucking_bots[encounter].cash -= current_esm * x
            fucking_bots[encounter].esm += current_esm
        print(fucking_bots[encounter].cash,fucking_bots[encounter].esm, names[cnt])
        encounter += 1
        cnt += 1
    s = ''
    if (offers[0]>=current_min) and (offers[0]>0)and((players[0].cash - (current_esm * offers[0])) > 0):
        players[0].cash -= current_esm * offers[0]
        players[0].esm += current_esm
        s = 'Банк продал вам ' + str(current_esm) + ' есм' + ' Ваш баланс: ' + str(players[0].cash)
    if s == '':
        s = 'Банк не одобрил ваше предложение о покупке есм' 
    condition.configure(text=s)
    condition.grid(column=0, row=0)
    print(current_min)
    
    
def get_bank():
    lot_condition.destroy()
    global prod, condition
    condition = Label(text="")
    prod = Button(text="Подать заявку на переработку есм в егп", command=sell_prod)
    get_bank_choice(offers, fucking_bots,players, current_rate)
    prod.grid(column=0, row=1)
     



    
    
 
def production(fucking_bots, players, bots, sending, factory_type):
    
    for fucking_bot in fucking_bots:
        if fucking_bot.esm >= 1:
            if fucking_bot.autofab == 0:
                while fucking_bot.cash > 4000:
                    fucking_bot.cash -= 2000
                    fucking_bot.esm -= 1
                    fucking_bot.egp += 1
            else:
                while fucking_bot.cash > 4500:
                    fucking_bot.cash -= 3000
                    fucking_bot.esm -= 2
                    fucking_bot.egp += 2
            print(fucking_bot.egp,fucking_bot.esm,fucking_bot.cash)
    f = True
    if (factory_type == 2) and (players[0].autofab == 0):
        f = False
    print(players[0].cash)
    if sending<=players[0].esm:
        if (factory_type == 1)and(sending<=players[0].fab):
            players[0].cash -= sending * 2000
            players[0].esm -= sending
            players[0].egp += sending
        if (factory_type == 2)and(f == True)and(sending<=players[0].autofab):
            players[0].cash -= sending * 3000
            players[0].esm -= sending
            players[0].egp += sending
    print(players[0].cash, 'ЕСМ= ',players[0].esm, 'ЕГП= ', players[0].egp)
    s = 'Вы имеете:\n' + str(players[0].cash) + '$\n' + str(players[0].esm) + ' есм\n' + str(players[0].egp) + ' егп'
    sell_info.configure(text=s)
    sell_info.grid(column=0, row=0)
    
            
          
def sell_prod():
    condition.destroy()
    prod.destroy()
    global egp_inf, egp_user, send_egp, wish, simple, auto, fact_info
    egp_inf = Entry(window, width=10)
    egp_user = Label(window, text="")
    send_egp = Button(text="отправить заявку", command=next_prod)
    simple = Radiobutton(window, text="Обычная фабрика",variable=fact, value=1)
    auto = Radiobutton(window, text="Автоматизированная фабрика",variable=fact, value=2)
    wish = Label(window, text="На каком типе \nфабрик будете перерабатывать \nесм в егп?")
    fact_info = Label(window, text="")
    egp_inf.grid(column=0, row=0)
    s = 'Ваш баланс: ' + str(players[0].cash)+ '$' + '\nУ вас имеется ' + str(players[0].esm) + ' есм'
    egp_user.configure(text=s)
    egp_user.grid(column=0, row=1)
    send_egp.grid(column=1, row=0)
    wish.grid(column=0, row=2)
    simple.grid(column=0, row=3)
    auto.grid(column=1, row=3)
    s = 'У вас имеется:\n' + ' обычные фабрики(переработка - 2000$): ' + str(players[0].fab)+ '\n' + ' автоматизированные фабрики(переработка - 3000$): ' + str(players[0].autofab) 
    fact_info.configure(text=s)
    fact_info.grid(column=0, row=4)
    

def next_prod():
    global sending
    sending = int(egp_inf.get())
    global selling_egp, sell_info
    sell_info = Label(window, text="")
    selling_egp = Button(text="Перейти к подаче заявки\n на продажу имеющихся егп", command=sell_egp)
    egp_inf.destroy()
    egp_user.destroy()
    send_egp.destroy()
    wish.destroy()
    global factory_type
    factory_type = fact.get()
    simple.destroy()
    auto.destroy()
    fact_info.destroy()
    print(factory_type)
    production(fucking_bots, players, bots, sending, factory_type)
    selling_egp.grid(column=0, row=1)

def sellebration(sell_offers,fucking_bots, cost_egp):
    enc = 1
    budget = 0
    current_egp = current_rate.get('EGP')
    current_max = current_rate.get('max_price')
    sell_offers[0] = cost_egp
    for fucking_bot in fucking_bots:
        if fucking_bot.egp >= 1: 
            budget = randint(current_max - 3000,current_max + 3000)
            sell_offers[enc] = budget
        else:
            sell_offers[enc] = 0
        enc += 1
    print('current_max', current_max)
    print(sell_offers)
    
def gang_bank_choice(sell_offers, fucking_bots, players, counting_egp):
    current_egp = current_rate.get('EGP')
    current_max = current_rate.get('max_price')
    print(current_egp)
    print(sell_offers)
    encounter = 0
    for x in sell_offers[1:]:
        if(x > 0)and(x <= current_max):
            if (fucking_bots[encounter].egp <= current_egp)and(fucking_bots[encounter].egp>=1):
                fucking_bots[encounter].cash += x
                fucking_bots[encounter].egp -= 1
            elif(fucking_bots[encounter].egp >= current_egp)and(fucking_bots[encounter].egp>=1):
                fucking_bots[encounter].cash += x
                fucking_bots[encounter].egp -= 1   
            encounter += 1
    f = False
    s = ''
    if counting_egp <= players[0].egp:
        f = True
    if(sell_offers[0] <= current_max)and(sell_offers[0] > 0)and(f == True):
        if counting_egp <= current_egp:
            players[0].cash += counting_egp * sell_offers[0]
            players[0].egp -= counting_egp
            s = 'Вы продали ' + str(counting_egp) + ' егп ' + '\nза ' + str(counting_egp * sell_offers[0]) + '$' + '\nВаш баланс: ' + str(players[0].cash) + '$\n' + 'У вас осталось ' + str(players[0].egp) + ' егп'
    if s == '':
        s = 'Вам не удалось заработать на продаже егп'
    print(players[0].cash, players[0].egp, s)
    bank_egp.configure(text=s)
    bank_egp.grid(column=0, row=0)
    print(bots, 'Боты гет банк')
    sell_offers = [0 for x in range((bots + 1))]
    offers = [0 for x in range((bots + 1))]
    
def sell_egp():
    sell_info.destroy()
    selling_egp.destroy()
    global txt_egp, egp_offer, cnt_egp, txt_cnt_egp, txt_egp_offer, accept
    cr_simple = Radiobutton(window, text="под обычную фабрику: 5.000$",variable=cred, value=1)
    cr_auto = Radiobutton(window, text="под автоматизированную фабрику: 10.000$",variable=cred, value=2)
    cr_no = Radiobutton(window, text="Отказываюсь от получения ссуды",variable=cred, value=3)
    credit_inf = Label(text="Если вы хотите получить ссуду, то укажите её размер.\n Если вы не хотите получить ссуду, то вы можете от неё отказаться")
    cr_application = Button(text="Далее", command=credit_aplication)
    cr_res = Label(text="")
    rep_inf = Label(text="")
    per_ssudi = Label(text="")
    egp_offer = Entry(window, width=10)
    cnt_egp = Entry(window, width=10)
    txt_egp = Label(window, text="")
    txt_cnt_egp = Label(window, text="кол-во егп")
    txt_egp_offer = Label(window, text="цена за егп")
    accept = Button(text="Передать заявку банку", command=acception)
    s = 'Вы имеете:\n' + str(players[0].cash) + '$\n' + str(players[0].egp) + ' егп'
    txt_egp.configure(text=s)
    txt_egp.grid(column=0, row=0)
    egp_offer.grid(column=0, row=1)
    cnt_egp.grid(column=0, row=2)
    txt_cnt_egp.grid(column=1, row=2)
    txt_egp_offer.grid(column=1, row=1)
    accept.grid(column=0, row=3)
    

def acception():
    global cost_egp, counting_egp
    cost_egp = int(egp_offer.get())
    counting_egp = int(cnt_egp.get())
    print('Цена: ', cost_egp, 'кол-во: ', counting_egp)
    txt_egp.destroy()
    egp_offer.destroy()
    cnt_egp.destroy()
    txt_cnt_egp.destroy()
    txt_egp_offer.destroy()
    accept.destroy()
    global credit_first, bank_egp
    bank_egp = Label(window, text="")
    credit_first = Button(text="Рассмотреть предложение \nполучения ссуд", command=ssudi)
    sellebration(sell_offers,fucking_bots, cost_egp)
    gang_bank_choice(sell_offers, fucking_bots, players, counting_egp)
    credit_first.grid(column=0, row=1)
    
def suud_percent(players,fucking_bots,investment):
    encounter = 1
    amount = 0
    delta = 0
    enc = 0
    for fucking_bot in fucking_bots:
        enc = 0
        if investment[encounter].get("got")!=0:
            amount = int(investment[encounter].get("got"))
            fucking_bot.cash -= 833
            delta = amount - 833
            enc = investment[encounter].get("month")-1
            investment[encounter].update(month=enc, got=delta)
        encounter += 1
    s = ''
    delta = 0
    enc = 0
    if investment[0].get("got")!=0:
        amount = int(investment[0].get("got"))
        players[0].cash -= 833
        delta = amount - 833
        enc = investment[0].get("month")-1
        investment[0].update(month=enc, got=delta)
        s = 'Вы погасили активную ссуду на: ' + str(833)
    if s == '':
        s = 'У вас нет активных ссуд'
    per_ssudi.configure(text=s)
    
def repayment_ssudi(players,fucking_bots,investment):
    enc = 1
    s = ''
    for bot in fucking_bots:
        if (investment[enc].get("got")!=0)and(investment[enc].get("month")==0):
            amount = investment[enc].get("got")
            bot.cash -= amount
            investment[enc].update(month=0, got=0)
        enc += 1
    if (investment[0].get("got")!=0)and(investment[0].get("month")==0):
        amount = investment[0].get("got")
        players[0].cash -= amount
        investment[0].update(month=0, got=0)
        s = 'Вы успешно погасили долг!'
    rep_inf.configure(text=s)
    
    
    
        
             
 
def be_invested(players,fucking_bots,investment, credit_value):
    encounter = 1
    for fucking_bot in fucking_bots:
        if (fucking_bot.cash >= 0)and(fucking_bot.cash <= 1500)and(investment[encounter].get("got")==0):
            investment[encounter].update(month=12, got=5000)
            fucking_bot.cash += 5000
        print(fucking_bots[encounter-1].cash)
        encounter += 1
    s = ''
    if credit_value == 1:
        if investment[0].get("got")==0:
            investment[0].update(month=12, got=5000)
            players[0].cash += 5000
            s = 'Получена ссуда в размере 5.000$\n на 12 месяцев\n' + 'Ваш баланс: ' + str(players[0].cash)
    elif credit_value == 2:
        if investment[0].get("got")==0:
            investment[0].update(month=12, got=10000)
            players[0].cash += 10000
            s = 'Получена ссуда в размере 10.000$\n на 15 месяцев\n' + 'Ваш баланс: ' + str(players[0].cash)
    if s == '':
        s = 'Вы отказались от ссуды в этом месяце или банк не одобрил получение ссуды\n' + 'Ваш баланс: ' + str(players[0].cash)
    cr_res.configure(text=s)   
    print(players[0].cash)
    print(investment)
    
    
def ssudi():
    bank_egp.destroy()
    credit_first.destroy()
    global credit_inf, cr_simple, cr_auto, cr_no, cr_application
    cr_simple = Radiobutton(window, text="под обычную фабрику: 5.000$",variable=cred, value=1)
    cr_auto = Radiobutton(window, text="под автоматизированную фабрику: 10.000$",variable=cred, value=2)
    cr_no = Radiobutton(window, text="Отказываюсь от получения ссуды",variable=cred, value=3)
    credit_inf = Label(text="Если вы хотите получить ссуду, то укажите её размер.\n Если вы не хотите получить ссуду, то вы можете от неё отказаться")
    cr_application = Button(text="Далее", command=credit_aplication)
    credit_inf.grid(column=0, row=0)
    cr_simple.grid(column=0, row=1)
    cr_auto.grid(column=0, row=2)
    cr_no.grid(column=0, row=3)
    cr_application.grid(column=0, row=4)
    
def credit_aplication():
    global credit_value
    credit_value = int(cred.get())
    credit_inf.destroy()
    cr_simple.destroy()
    cr_auto.destroy()
    cr_no.destroy()
    cr_application.destroy()
    global per_ssudi, rep_inf, cr_res, build
    cr_res = Label(text="")
    rep_inf = Label(text="")
    per_ssudi = Label(text="")
    build = Button(text="Перейти к подаче заявки\n на строительство фабрик", command=build_inf)
    suud_percent(players,fucking_bots,investment)
    per_ssudi.grid(column=0, row=0)
    repayment_ssudi(players,fucking_bots,investment)
    rep_inf.grid(column=0, row=1)
    be_invested(players,fucking_bots,investment, credit_value)
    cr_res.grid(column=0, row=2)
    build.grid(column=0, row=3)
 
def build_factories(players, fucking_bots, buildings, build_value, month):
    enc = 1
    if month != 1:
        for bot in fucking_bots:
            for i in buildings[enc]:
                if (i.get('remaining') != 0) and (i.get('typee') != 0):
                    i.update(remaining=int(i.get('remaining')-1), typee=int(i.get('typee')))
                    if i.get('remaining')==0:
                        if i.get('typee')==1:
                            bot.fab += 1
                            i.update(remaining=0, typee=0)
                        elif i.get('typee')==2:
                            bot.autofab += 1
                            i.update(remaining=0, typee=0)
        enc += 1
    s1 = ''
    if month != 1:
        for i in buildings[0]:
            if (i.get('remaining') != 0) and (i.get('typee') != 0):
                i.update(remaining=int(i.get('remaining')-1), typee=int(i.get('typee')))
                if i.get('remaining')==0:
                    if i.get('typee')==1:
                        players[0].fab += 1
                        i.update(remaining=0, typee=0)
                        s1 = 'Теперь вы можете\n ещё одну обычную фабрику'
                    elif i.get('typee')==2:
                        players[0].autofab += 1
                        i.update(remaining=0, typee=0)
                        s1 = 'Теперь вы можете\n ещё одну автоматизированную фабрику'
    if s1 == '':
        s1 = 'Нет информации о построенных фабриках в этом месяце'
    magic_wand = 0
    magic_wand = randint(1, 2)
    counter = 1
    for bot in fucking_bots:
        if magic_wand == 1:
            if bot.cash - 5000 > 1000:
                for i in buildings[counter]:
                    if i.get('remaining') == 0 and i.get('typee') == 0:
                        i.update(remaining=5, typee=1)
                        bot.cash -= 5000
                        #fucking_bot.fab += 1
                        break
                counter += 1
        if magic_wand == 2:
            if bot.cash - 10000 > 1000:
                for i in buildings[counter]:
                    if i.get('remaining') == 0 and i.get('typee') == 0:
                        i.update(remaining=7, typee=2)
                        bot.cash -= 10000
                        #fucking_bot.autofab += 1
                        break
                counter += 1
    s = ''
    amo = 0
    typ = 0
    typ_mon = 0
    f = False
    if(build_value==1)and(players[0].cash >= 5000):
        f = True
        typ = 1
        typ_mon = 5
        amo = 5000
        s = 'Ваша заявка подтверждена\n на строительство обычной фабрики'
    elif(build_value==2)and(players[0].cash >= 10000):
        f = True
        typ = 2
        typ_mon = 7
        amo = 10000
        s = 'Ваша заявка подтверждена\n на строительство автоматизированной фабрики'
    elif(build_value==3):
        f = False
    if f:
        for i in buildings[0]:
            if i.get('remaining') == 0 and i.get('typee') == 0:
                i.update(remaining=typ_mon, typee=typ)
                players[0].cash -= amo
                break
    if s == '':
        s = 'Вы отказались от строительства\n либо банк не одобрил вашу заявку'
    s += '\nСписание: ' + str(amo) + '\nВаш баланс: ' + str(players[0].cash)
    if month != 1:
        s += '\n' + s1
    apl_inf.configure(text=s)
    print(buildings)
    month += 1
                
                
                
        
    
def build_inf():
    per_ssudi.destroy()
    rep_inf.destroy()
    cr_res.destroy()
    build.destroy()
    s = 'Вы имеете:\n' + str(players[0].cash) + '$\n' + 'Обычные фабрики: ' + str(players[0].fab) + '\nАвтоматизированные фабрики: ' + str(players[0].autofab) + '\nСтоимость постройкти обычной фабрики: 5.000$ \nпроцесс постройки составляет 5 месяцев\n' + 'Стоимость постройкти автоматизированной фабрики: 10.000$ \nпроцесс постройки составляет 7 месяцев'
    global pl_stuff, bui, buildf_simple, buildf_auto, buildf_no, aplic_bui
    pl_stuff = Label(text="")
    bui = Label(text="Выберите, что хотите построить.")
    buildf_simple = Radiobutton(window, text="Обычная фабрика",variable=build_f, value=1)
    buildf_auto = Radiobutton(window, text="Автоматизированная фабрика",variable=build_f, value=2)
    buildf_no = Radiobutton(window, text="Отказываюсь от строительства фабрик",variable=build_f, value=3)
    aplic_bui = Button(text="Подать заявку на строительство", command=build_application )
    pl_stuff.configure(text=s)
    pl_stuff.grid(column=0, row=0)
    bui.grid(column=0, row=1)
    buildf_simple.grid(column=0, row=2)
    buildf_auto.grid(column=0, row=3)           
    buildf_no.grid(column=0, row=4)        
    aplic_bui.grid(column=0, row=5)
    
def build_application():
    global build_value
    build_value = int(build_f.get())
    pl_stuff.destroy()
    bui.destroy()
    buildf_simple.destroy()
    buildf_auto.destroy()
    buildf_no.destroy()
    aplic_bui.destroy()
    global apl_inf, banking
    apl_inf = Label(text="")
    banking = Button(text="Приступить к следующему месяцу игры", command=pay)
    build_factories(players, fucking_bots, buildings, build_value, month)
    apl_inf.grid(column=0, row=0)
    
    banking.grid(column=0, row=1)
  
    
    

def but1():  
    lbl.configure(text="")
    name = txt.get()
    #print(name) ник игрока
    txt.destroy()
    btn.destroy()
    inf.grid(column=0, row=0)
    und.grid(column=0, row=2)
    names.append(name)
def begin():
    lbl.grid(column=0, row=0)  
    txt.grid(column=1, row=0)
    btn.grid(column=2, row=0)
    beg.destroy()
def unders():
    und.destroy()
    inf.destroy()
    choi.grid(column=0, row=0)
    two.grid(column=0, row=1)
    thr.grid(column=0, row=2)
    fou.grid(column=0, row=3)
    nex.grid()
    
def nextt():
    global bots
    bots = 0
    nex.destroy()
    two.destroy()
    thr.destroy()
    fou.destroy()
    choi.destroy()
    bots = var.get()
    if bots==2:
        names.append(bot1)
        names.append(bot2)
    if bots==3:
        names.append(bot1)
        names.append(bot2)
        names.append(bot3)
    if bots==4:
        names.append(bot1)
        names.append(bot2)
        names.append(bot3)
        names.append(bot4)
    print(bots, 'БОТЫ')
    global sell_offers, investment, buildings, players, offers, current_rate 
    sell_offers = [0 for x in range((bots + 1))]
    investment = [{'month': 0, 'got': 0} for x in range((bots + 1))]
    buildings = [[{'remaining': 0, 'typee': 0} for i in range(6)] for x in range((bots + 1))]            
    players = [Players(2, 0, 4, 2, 10000), [Players(2, 0, 4, 2, 10000) for x in range(bots)]]
    offers = [0 for x in range((bots + 1))]
    global fucking_bots
    fucking_bots = players[1]
    #print(players)
    #while
    month = 0
    
    banking.grid(column=0, row=0)
    
    
    
    

bank_instances = [{'ECM': 1.0, 'min_price': 800, 'EGP': 3.0, 'max_price': 6500},
{'ECM': 1.5, 'min_price': 650, 'EGP': 2.5, 'max_price': 6000},
{'ECM': 2.0, 'min_price': 500, 'EGP': 2.0, 'max_price': 5500},
{'ECM': 2.5, 'min_price': 400, 'EGP': 1.5, 'max_price': 5000},
{'ECM': 3.0, 'min_price': 300, 'EGP': 1.0, 'max_price': 4500}]
names = []
bot1 = 'bot1'
bot2 = 'bot2'
bot3 = 'bot3'
bot4 = 'bot4'
window = Tk()  
window.title("The Best Game Ever")  
window.geometry('550x550')
name = ''
lbl = Label(window, text="Nickname:")  
txt = Entry(window,width=10)    
btn = Button(window, text="Enter", command=but1)
beg = Button(window, text="Начать игру",  command=begin)
beg.grid(column=2, row=0)
inf = Label(window, text="Начальные ресурсы игрока: \n2 обычные фабрики \n4 единицы сырья и материалов \n2 единицы готовой продукции \n10.000$")
und = Button(window, text="Ознакомился", command=unders)
choi = Label(window, text="Выберите количество ботов:")
var = IntVar()
var.set(2)
two = Radiobutton(window, text="2",variable=var, value=2)
thr = Radiobutton(window, text="3",variable=var, value=3)
fou = Radiobutton(window, text="4",variable=var, value=4)
nex = Button(window, text="Переход к игре", command=nextt)
money1 = Label(window, text="")
money2 = Label(window, text="")
banking = Button(text="Приступить к первому месяцу игры", command=pay)
information = Button(text="Next", command=listT)
player_cash = Button(text="Предложить банку цену\n для покупки есм", command=lot)
player_lot = Entry(window, width=10)
lot_done = Button(text="Предложить цену", command=lot_next)
lot_condition = Button(text="Узнать состояние транзакции", command=get_bank)
condition = Label(text="")
prod = Button(text="Подать заявку на переработку есм в егп", command=sell_prod)
egp_inf = Entry(window, width=10)
egp_user = Label(window, text="")
send_egp = Button(text="отправить заявку", command=next_prod)
bankrot = Label(text="")

fact = IntVar()
fact.set(1)
simple = Radiobutton(window, text="Обычная фабрика",variable=fact, value=1)
auto = Radiobutton(window, text="Автоматизированная фабрика",variable=fact, value=2)
wish = Label(window, text="На каком типе \nфабрик будете перерабатывать \nесм в егп?")
fact_info = Label(window, text="")

sell_info = Label(window, text="")
selling_egp = Button(text="Перейти к подаче заявки\n на продажу имеющихся егп", command=sell_egp)

egp_offer = Entry(window, width=10)
cnt_egp = Entry(window, width=10)
txt_egp = Label(window, text="")
txt_cnt_egp = Label(window, text="кол-во егп")
txt_egp_offer = Label(window, text="цена за егп")
accept = Button(text="Передать заявку банку", command=acception)

bank_egp = Label(window, text="")
credit_first = Button(text="Рассмотреть предложение \nполучения ссуд", command=ssudi)

cred = IntVar()
cred.set(1)
cr_simple = Radiobutton(window, text="под обычную фабрику: 5.000$",variable=cred, value=1)
cr_auto = Radiobutton(window, text="под автоматизированную фабрику: 10.000$",variable=cred, value=2)
cr_no = Radiobutton(window, text="Отказываюсь от получения ссуды",variable=cred, value=3)
credit_inf = Label(text="Если вы хотите получить ссуду, то укажите её размер.\n Если вы не хотите получить ссуду, то вы можете от неё отказаться")
cr_application = Button(text="Далее", command=credit_aplication)
cr_res = Label(text="")
rep_inf = Label(text="")
per_ssudi = Label(text="")

build = Button(text="Перейти к подаче заявки\n на строительство фабрик", command=build_inf)
pl_stuff = Label(text="")
bui = Label(text="Выберите, что хотите построить.")
build_f = IntVar()
build_f.set(1)
buildf_simple = Radiobutton(window, text="Обычная фабрика",variable=build_f, value=1)
buildf_auto = Radiobutton(window, text="Автоматизированная фабрика",variable=build_f, value=2)
buildf_no = Radiobutton(window, text="Отказываюсь от строительства фабрик",variable=build_f, value=3)
aplic_bui = Button(text="Подать заявку на строительство", command=build_application )
apl_inf = Label(text="")

window.mainloop()




