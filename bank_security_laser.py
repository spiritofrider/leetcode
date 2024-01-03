def bank_security_laser(arr: list) -> int:
    store = {}
    result = 0
    for i in arr:
        if i.count("1") > 0:
            store[i] = i.count("1")
    temp = list(store.values())
    for i in range(1, len(temp)):
        result += temp[i-1]*temp[i]
    return result

print(bank_security_laser(["011001","000000","010100", "001000"]))
print(bank_security_laser(["000", "111", "000"]))