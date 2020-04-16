list = [7,10,7,0,9,11,0,17,]
# list = [69,40,0,0,90,0,1]
def special_sort(list):
    atlag = sum(list)/len(list)
    smh = 0
    seged = []
    # list=[tag for tag in list if (tag>atlag or tag==0)]
    for elem in list:
        if elem==0:
            smh+=1
        elif elem<atlag:
            seged.append(elem)
    list.sort()
    for tag in seged:
        list.remove(tag)

    while smh>0:
        list.remove(0)
        list.append(0)
        smh-=1

special_sort(list)
print(list)