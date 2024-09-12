import random as r

season = False
stock1_price_list = []
stock2_price_list = []
stock3_price_list = []
stock4_price_list = []

def stock_price_init(val1, val2, val3, val4):
    stock1_price_list.append(val1)
    stock1_price_list.append(stock1_price_list[-1])
    stock1_price_list.append(stock1_price_list[-1])
    stock2_price_list.append(val2)
    stock2_price_list.append(stock2_price_list[-1])
    stock2_price_list.append(stock2_price_list[-1])
    stock3_price_list.append(val3)
    stock3_price_list.append(stock3_price_list[-1])
    stock3_price_list.append(stock3_price_list[-1])
    stock4_price_list.append(val4)
    stock4_price_list.append(stock4_price_list[-1])
    stock4_price_list.append(stock4_price_list[-1])



def stock1_price_update():
    decision = r.randint(1,2) # 1 -> upper / 2 -> lower
    x = stock1_price_list[-3]
    y = stock1_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 15
        b += 20
    else:
        a -= 20
        b -= 15
        if a <= 0 or b <= 0:
            a += 30
            b += 40

    val = r.randint(a,b)

    stock1_price_list.append(val)

    return stock1_price_list

def stock2_price_update():
    decision = r.randint(1,2) # 1 -> upper / 2 -> lower
    x = stock2_price_list[-3]
    y = stock2_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 15
        b += 20
    else:
        a -= 20
        b -= 15
        if a <= 0 or b <= 0:
            a += 30
            b += 40

    val = r.randint(a,b)

    stock2_price_list.append(val)

    return stock2_price_list

def stock3_price_update():
    decision = r.randint(1,2) # 1 -> upper / 2 -> lower
    x = stock3_price_list[-3]
    y = stock3_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 15
        b += 20
    else:
        a -= 20
        b -= 15
        if a <= 0 or b <= 0:
            a += 30
            b += 40

    val = r.randint(a,b)

    stock3_price_list.append(val)

    return stock3_price_list

def stock4_price_update():
    decision = r.randint(1,2) # 1 -> upper / 2 -> lower
    x = stock4_price_list[-3]
    y = stock4_price_list[-1]

    if x <= y:
        a = x
        b = y
    else:
        a = y
        b = x

    if decision == 1:
        a += 15
        b += 20
    else:
        a -= 20
        b -= 15
        if a <= 0 or b <= 0:
            a += 30
            b += 40

    val = r.randint(a,b)

    stock4_price_list.append(val)

    return stock4_price_list
