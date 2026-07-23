def eating_mangoes(num):
    if num==0:
        print("No mangoes left.Done")
        return
    else:
        print(f"{num} mangoes left. Eating one.")
        eating_mangoes(num-1)

eating_mangoes(3)