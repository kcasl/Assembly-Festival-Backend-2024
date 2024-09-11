from stock_price_management import *

val = r.randint(500,1000)
stock1_price_init(val)

print(stock1_price_list)

for i in range(1, 900):
    print(stock1_price_update())

print(stock1_price_list)

