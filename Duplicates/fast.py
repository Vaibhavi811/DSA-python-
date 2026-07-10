# Find Dupliactes-- Fast method

numbers= [2,4,6,8,8,11]

def find_Duplicates(numbers):
    seen= set()

    for num in numbers:
        if num in seen:
            return True
        else:
            seen.add(num)

    return False

result= find_Duplicates(numbers)

if result:
    print("Duplicates found")
else:
    print("No Duplicates")