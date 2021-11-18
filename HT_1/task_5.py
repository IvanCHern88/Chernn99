"""
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
"""        
        
def toHex(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    return toHex(rest) + digits[x]

result = []
for i in list(input('Введіть числа:').split(",")):
    result.append(toHex(int(i)))

print(", ".join(result))

