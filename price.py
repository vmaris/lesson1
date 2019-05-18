def format_price(price):
    price = int(price)
    format_price = f'Price: {price} RUB'
    return format_price

price1 = float(input('Enter the price '))
print(format_price(price1))