# WAP to find the two numbers whose product is maximum all the pairs in given list use python set.

numbers=[2,4,5,6,7,8,3]
nums=list(set(numbers))
max_product=nums[0]*nums[1]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        product=nums[i]*nums[j]
        if product>max_product:
            max_product=product
            paire=(nums[i],nums[j])
            
print('Paire which has maximum product:',paire)