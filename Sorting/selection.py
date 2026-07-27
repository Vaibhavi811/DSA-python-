# Selection Sort -- find the minimum number and then swap
def selection(numbers):
    for i in range(len(numbers)-1):
        min_index= i
        for j in range(i+1,len(numbers)):
            if numbers[min_index]>numbers[j]:
                min_index= j
        numbers[i],numbers[min_index]= numbers[min_index],numbers[i]

    return numbers

numbers=[99,11,100,5,63]
print(selection(numbers))

            