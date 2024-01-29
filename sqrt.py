
# minha solução, só passou em um teste

# def sqrt(x):
#     count = 0
#     for i in range(1, x + 1):
#         if i * i == x:
#             count += 1
#             return i

# x = 6
# print(sqrt(x))

# solução correta

def mysqrt(x):
    
    left = 0
    right = x 

    while left <= right:
        mid = (left + right) // 2  # mid 3
       
        if mid * mid < x:
            left = mid +1 # 4
         
        elif mid * mid > x:
            right = mid -1 # 3
           
        else:
            return mid
        
    return right

x = 6
print(mysqrt(x))
