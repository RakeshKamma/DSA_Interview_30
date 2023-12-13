sample=[0,1,0,2,1,0,3,1,0,1,2]

#TIme complexity -O(n^2)
#space complexity-O(1)
def trap_rainwater(sample):
    final_result =0

    for i in range(1,len(sample)-1):
        current = sample[i]

        right_max = max(sample[i+1:])
        left_max = max(sample[:i])

        if right_max> current and left_max> current:
            final_result += min(left_max,right_max) - current


    return final_result



print(trap_rainwater(sample))