# Counting frequency of orders in a restaurant
foods=["idli","idli","dosa",'maggie','maggie','noodles']

d={}

for food in foods:
    if food in d:
        d[food]+=1
    else:
        d[food]=1

print(d)