def palindomer(n: int):
    if (n < 0) or (n > 0 and n % 10 == 0):
        return False
    
    half = 0
    while n > half:
        half = (half * 10) + n % 10 # 12
        n = n // 10 # 12
        if n == half or n == half // 10:
            return True
        
        

print(palindomer(121))

     







