# Bubble Sort -- swapping at each position
def Bubble(numbers):
    # for no of passes
    for i in range(len(numbers)-1):
        # for individual sorting
        for j in range(1,len(numbers)-i):
            if numbers[j-1]>numbers[j]:
                numbers[j-1],numbers[j]=numbers[j],numbers[j-1]

    return numbers

numbers=[20,70,45,99,22,100]
result= Bubble(numbers)
print(result)