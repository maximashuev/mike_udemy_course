def advertise_decision(adv: tuple):
    # print(adv)

    des=[int(i) for i in list(adv.split(" "))]
    # print(des)
    if des[0]<(des[1]-des[2]):
        print('Запускать')
        return ('Запускать')
    elif des[0]==(des[1]-des[2]):
        print('Без разницы')
        return ('Без разницы')
    else:
        des[0]>(des[1]-des[2])
        print('Не запускать')
        return ('Не запускать')



advertise_decision("0 100 70")
advertise_decision("100 130 30")