def itoa(number, res):

    while True:
        temp = number % 10
        res = chr(ord('0') + temp) + res
        number = number // 10
        if number == 0:
            break
    return res


number = 4567
res = ''

print(number,type(number))
string = itoa(number,res)
print(string,type(string))

