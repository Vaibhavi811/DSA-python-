# Method 1
prices=[2,4,6,1,7,3,5]

def sum_three(prices):
    max=0
    left=0

    for right in range(2,len(prices)):
        if max < sum(prices[left:right+1]):
            max= sum(prices[left:right+1])
            index= left

        left+=1

    return max, index

m,i= sum_three(prices)
print(m,i)

# Method 2
prices= [2,4,6,1,7,3,5]

def sum_three2(prices):
    max= 0

    for i in range(len(prices)-2):
        if max < sum(prices[i:i+3]):
            max= sum(prices[i:i+3])
            index= i

    return max, index

m1,i1= sum_three2(prices)
print(m1,i1)

# Method 3
def sum_three3(prices,windowsize):
    current_total=sum(prices[0:windowsize])
    best_total= current_total

    print("Window 1:",prices[0:windowsize])

    for i in range(windowsize,len(prices)):
        left=prices[i-windowsize]
        right=prices[i]

        current_total=current_total-left+right
        if best_total<current_total:
            best_total= current_total

        print("Window:",prices[i-windowsize+1:i+1])

    return best_total

result=sum_three3(prices,3)
print("Sum:",result)
