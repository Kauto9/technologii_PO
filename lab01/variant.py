name = input("Введите своё имя - ")
order = input("Введите название заказа - ")

item1 = input("Введите название 1 товара - ")
priceItem1= float(input("Введите цену 1 товара в рублях - "))
amountItem1= int(input("Введите количество 1 товара - "))

item2 = input("Введите название 2 товара - ")
priceItem2= float(input("Введите цену 2 товара в рублях - "))
amountItem2= int(input("Введите количество 2 товара - "))

delivery = float(input("Введите стоимость доставки - "))

deposite= float(input("Введите внесённую сумму - "))

discount= float(input("При наличии введите процент скидки - "))

cost1= priceItem1*amountItem1
cost2= priceItem2*amountItem2

discountAmount= (cost1+cost2)/100*discount
withDiscount= (cost1+cost2)-discountAmount
newTotal= withDiscount+delivery

print(f"Заказ - {order}, заказчик - {name}")
print(f"{item1}|{amountItem1}|{priceItem1:.2f}|{cost1:.2f}")
print(f"{item2}|{amountItem2}|{priceItem2:.2f}|{cost2:.2f}")
print(f"Скидка составляет {discountAmount:.2f} руб")
print(f"Итоговая сумма заказа без доставки - {cost1+cost2:.2f}, со скидкой - {withDiscount:.2f}, \n"
      f"с доставкой без скидки - {cost1+cost2+delivery:.2f}, c доставкой и скидкой - {newTotal:.2f}")
print(f"Всего товаров заказано - {amountItem1+amountItem2}")
print(f"Сдача составляет {deposite-newTotal:.2f}")