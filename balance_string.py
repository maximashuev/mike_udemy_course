

def count_balance(string: str):
    score = 0
    c = 0
    rng = range(len(string))
    for i in rng:
        if string[i] == string[0]:
            score += 1
        else:
            score += -1
        if score == 0:
            c += 1
    print(c)
    return c

count_balance("ASAASSASAS")
count_balance("AAASSAA")
count_balance("ASSAASSSAASASAS")
