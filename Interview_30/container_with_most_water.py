#brute force
#n - length of sample
# time complexity - O(n^2)
# space complexity - O(1)
def max_water(sample):
    max_area=0
    for a in range(len(sample)):
        for b in range(a+1,len(sample)):
            min_height = min(sample[a],sample[b])
            width = b-a
            area=(min_height*width)
            max_area = max(max_area,area)
            
    return max_area


#optimized
#n - length of sample
# time complexity - O(n)
# space complexity - O(1)

def max_water(numbers):
    if len(numbers) ==0: return 0
    i=max_area=0
    j=width=len(numbers)-1
    while(i!=j):
        area =min(numbers[i],numbers[j])*width
        max_area= max(max_area,area)
        if(numbers[i]<numbers[j]):
            i+=1
            width-=1
        else:
            j-=1
            width-=1
    return max_area

print(max_water([]))
print(max_water([7]))
print(max_water([1,3,4,2]))

