


s = "   fly me   to   the moon "
size = len(s)
size_last_w = 0




for i in range(size-1, -1, -1):
    if s[i] != " ":
        size_last_w += 1
    
    elif size_last_w > 0:
        break

print(size_last_w)
        
        
    
    


   
     