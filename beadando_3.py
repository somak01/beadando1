list = [7,10,7,0,9,11,0,17]

def special_sort(list):
    atlag = sum(list)/len(list)
    flag=0
    flag_l = []
    for i in range(len(list)):
        if list[i]==0:
            flag+= 1
            if list[i] not in flag_l:
                flag_l.append(list[i])
        if list[i]<atlag:
            if list[i] not in flag_l:
                flag_l.append(list[i])
    for tag in flag_l:
        list.remove(tag)
    list.sort()
    while flag>0:
        list.append(0)
        flag-=1
    return list
print(special_sort(list))
