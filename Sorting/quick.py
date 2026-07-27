# Quick Sort -- select an element as pivot and then sort accordingly
# Time Complexity -- O(nlogn)

def quick(numbers):
    if len(numbers)<=1:
        return numbers
    
    last_index= len(numbers)-1
    left=[]
    right=[]


    for i in range(len(numbers)-1):
        if numbers[i]> numbers[last_index]:
            right.append(numbers[i])
        else:
            left.append(numbers[i])

    print(f"Splitting:{numbers}")
    print(f"Left:{left}")
    print(f"Right:{right}")
    print()

    left_sort= quick(left)
    right_sort= quick(right)

    sorted_list= left_sort + [numbers[last_index]] + right_sort
    print("Sorted:",sorted_list)

    return sorted_list

numbers=[17,8,27,5,26,11,46]
print(quick(numbers))