# Tower of Hanoi -- moving disc from source rod to destination rod using auxiliary rod in the same order (largest at the bottom)

def toh(src,aux,dest,num):
    if num==1:
        print(f"Disk moves from {src} to {dest}")
        return

    toh(src,dest,aux,num-1)
    print(f"Disk moves from {src} to {dest}")

    toh(aux,src,dest,num-1)

toh("Source","Auxiliary","Destination",3)