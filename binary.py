       # 2 ** 0 = 1                              somar = 4

a = "11"       #  2 ** 0   = 1  #  2 ** 1 = 2 
b = "1" 


def  addBinary(a: str, b: str):
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        
        i -= 1
        print(i)
      if j >= 0:
        carry += int(b[j])
        
        j -= 1
        print(j)
      s.append(str(carry % 2))
      carry //= 2 

    return ''.join(reversed(s))



print(addBinary(a, b))






