

def plus_one(digits) -> list:


    for i in range(len(digits) -1, -1, -1):
        
        
        if digits[i] == 9:
            digits[i] = 0
            
        
        else:
            digits[i] += 1
            return digits
            

    if digits[0] == 0:
        digits.insert(0,1)
        return digits
    
digits = [1,3,5]      
print(plus_one(digits))


        
    
   
    

  
    

    
    
    