def count_balance(string: str):
    print(string)
    res, count = 0, 0
    for c in string:
        count += 1 if c == string[0] else -1
        if count == 0:
            res += 1
    print(res)
    return res


count_balance("ASAASSASAS")
count_balance("AAASSSA")
