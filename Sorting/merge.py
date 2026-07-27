# Merge Sort -- Divide, Conquer, Merge/Combine
def combine(left,right):
    left_ptr=0
    right_ptr=0
    final=[]

    while left_ptr<len(left) and right_ptr<len(right):
        if left[left_ptr]> right[right_ptr]:
            final.append(right[right_ptr])
            right_ptr+=1
        else:
            final.append(left[left_ptr])
            left_ptr+=1
    
    remaining_left= left[left_ptr:]
    remaining_right= right[right_ptr:]

    final= final + remaining_left + remaining_right
    return final

def Merge(numbers):
    if len(numbers)==1:
        return numbers
    
    middle= len(numbers)//2
    left_grp=numbers[:middle]
    right_grp= numbers[middle:]

    print("Splitting:",numbers)
    print("Left:",left_grp)
    print("Right:",right_grp)
    print()

    left_sort=Merge(left_grp)
    right_sort=Merge(right_grp)

    sorted_list= combine(left_sort,right_sort)
    print("Sorted:",sorted_list)
    print()
    return sorted_list

numbers=[17,8,27,5,26,11,46]
print(Merge(numbers))