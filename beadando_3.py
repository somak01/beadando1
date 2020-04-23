# list = [7,10,7,0,9,11,0,17,]
# list = [69,40,0,0,90,0,1]
# list = [0,0,0,0,0,0,0,0,1]
list = []
def special_sort(list):
    if len(list)==0:
        return list
    atlag = sum(list)/len(list)
    smh = 0
    seged = []
    # list=[tag for tag in list if (tag>atlag or tag==0)]
    for elem in list:
        if elem<atlag:
            seged.append(elem)
    list.sort()
    print(seged)
    for tag in seged:
        if tag==0:
            list.remove(tag)
            list.append(tag)
        else:
            list.remove(tag)


special_sort(list)
print(list)