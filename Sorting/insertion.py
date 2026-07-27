# Insertion Sort -- pick a card and place it at correct position
def Insertion(numbers):
    for i in range(1,len(numbers)):
        key= numbers[i]
        j= i-1

        while j>=0 and numbers[j]> key:
            numbers[j+1]= numbers[j]
            j-=1

        numbers[j+1]= key
    return numbers

numbers=[27,11,5,8,17]
print(Insertion(numbers))
       