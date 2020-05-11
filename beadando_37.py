# list = [7,10,7,0,9,11,0,17,15,16,12]
# list = [68,40,0,0,90,0,1]
list = [7,10,0,9,11,0,17]
# list = [0,0,0,0,0,0,0,0,1]
# list = []
def sorting(list):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]

def special_sort(list):
    if len(list)==0:
        return list
    atlag = sum(list)/len(list)
    seged = []
    for elem in list:
        if elem<atlag:
            seged.append(elem)
    sorting(list)
    for tag in seged:
        if tag==0:
            list.remove(tag)
            list.append(tag)
        else:
            list.remove(tag)

# print(list)
special_sort(list)
print(list)