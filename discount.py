def discounted(price, discount, max_discount = 20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
       raise ValueError(" Скидка не может быть больше 99% !")
    if discount >= max_discount: 
       price_with_discount = price
    else:
       price_with_discount = price - price*discount/100
    return price_with_discount

