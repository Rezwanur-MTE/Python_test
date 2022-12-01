print("Hello World")
print("-------------------------------------------------")

def sum(x,y,z):
    if x==y or y==z or x==z : 
        sum=0
    else: 
        sum=x+y+z
    return sum

print("Sum test is ", sum(5,3,2))


print("----------------------------------------------------")

def test(nums):
    return nums.count(19)==2 and nums.count(5)>=3

nums=[19,18,19,6,5,7,6,5,0,5]
print("The original list is: ",nums) 

print("After checking condition :", test(nums))