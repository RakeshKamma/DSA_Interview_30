

#brute force
#n - length of numbers
# time complexity - O(n^2)
# space complexity - O(1)
def two_sum(target,numbers):
    for a in range(len(numbers)):
        remiander = target- numbers[a]
        for b in range(a+1,len(numbers)):
            if remiander==numbers[b]:
                return [a,b]
          
    return None

# optimized
# n - length of numbers
# time complexity - O(n)
# space complexity - O(n)
def two_sum_opt(target,numbers):
    result= {}
    for a,i in enumerate(numbers):
        remainder = target - i
        if i in result:
            return [result[i],a]
        else:
            result[remainder] = a

    return None

print(two_sum(11,[]))
print(two_sum(11,[1]))
print(two_sum(11,[1,3,7,9,2]))

print(two_sum_opt(11,[]))
print(two_sum_opt(11,[1]))
print(two_sum_opt(11,[1,3,7,9,2]))