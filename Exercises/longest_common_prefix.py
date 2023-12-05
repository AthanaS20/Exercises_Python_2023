nums = [10,2,5,6] 
target = 11

for i in range(0, len(nums)):
    for j in range(1, len(nums)):
        soma = nums[i] + nums[j]
        if soma == target:
            print(i, j)
        
            

            


