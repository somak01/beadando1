valami = 'AAAABBBCCDAAA'

def code(szo):
    new_str = ''
    db = 0
    tmp = szo[0]
    for i in range(0, len(szo)):
        if szo[i]==tmp:
            db+=1
        else:
            new_str+=str(db)+tmp
            db=0
            tmp=szo[i]
            db+=1
    new_str+=str(db)+tmp
    return new_str
def code_to_dict(code):
    list_values = []
    list_keys =[]
    for i in range(1,len(code), 2):
        list_keys.append('part'+str((i+1)//2))
        list_values.append(code[i-1:i+1])
    dictionary =dict(zip(list_keys, list_values))
    print(dictionary)
code_to_dict(code(valami))

