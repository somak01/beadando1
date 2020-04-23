valami = 'AAAAAABBBBCCCCAA'

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
    list = []
    for i in range(len(code)):
        list.append(code[i:i+1])
    return list