import random as r
import threading

stock1_price_list = []
stock2_price_list = []
stock3_price_list = []
stock4_price_list = []

stock1_return = []
stock2_return = []
stock3_return = []
stock4_return = []

# format = {'open' : 1, 'high' : 1, 'low' : 1, 'close' : 1}

def stock_price_init(val1, val2, val3, val4):
    stock1_price_list.clear()
    stock2_price_list.clear()
    stock3_price_list.clear()
    stock4_price_list.clear()
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

def root_update():
    stock1_price_update()
    stock2_price_update()
    stock3_price_update()
    stock4_price_update()

    if len(stock1_price_list) > 100:
        return "라운드가 종료되었습니다."
    threading.Timer(6, root_update).start()

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

    res = {'open': stock1_price_list[-2], 'high': stock1_price_list[-2], 'low': stock1_price_list[-1],
           'close': stock1_price_list[-1]}
    stock1_return.append(res)

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

    res = {'open' : stock2_price_list[-2], 'high' : stock2_price_list[-2], 'low' : stock2_price_list[-1], 'close' : stock2_price_list[-1]}
    stock2_return.append(res)

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

    res = {'open': stock3_price_list[-2], 'high': stock3_price_list[-2], 'low': stock3_price_list[-1],
           'close': stock3_price_list[-1]}
    stock3_return.append(res)

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

    res = {'open': stock4_price_list[-2], 'high': stock4_price_list[-2], 'low': stock4_price_list[-1],
           'close': stock4_price_list[-1]}
    stock4_return.append(res)

    return stock4_price_list
