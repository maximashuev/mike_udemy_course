import csv

avg_sale_price = 0
count=0
with open('input.csv') as csvfile:
    re = csv.DictReader(csvfile)
    for line in re:
        count+=1
        avg_sale_price+=float(line["SALE_PRICE"])
avg_sale_price=avg_sale_price/count
# В конце задания нужно вывести среднюю стоимость продажи, округлив до 2х знаков после запятой.
# Так как ответ можно подобрать и просто вывести его на экран, при проверке производятся математические операции над данными, так что просто написать число после падения теста не выйдет и оно всегда будет разным, но вы же не будете так делатть ;)
print(round(avg_sale_price, 2))