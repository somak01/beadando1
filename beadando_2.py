valami = 'AABBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC'

def code_to_dict(szo):
    try:
        dictionary = {}
        seged = [szo[0]]
        db = 0
        tmp = szo[0]
        for i in range(0, len(szo)):
            if szo[i]==tmp:
                db+=1
            else:
                seged.append(szo[i])
                if tmp not in dictionary:
                    dictionary[tmp] = [str(db)]
                    db=0
                    tmp=szo[i]
                    db+=1
                else:
                    dictionary[tmp].append(str(db))
                    db = 0
                    tmp = szo[i]
                    db+=1
        if tmp not in dictionary:
            dictionary[tmp]=[str(db)]
        else:
            dictionary[tmp].append(str(db))
        kimenet = ''
        for ch in seged:
            if ch not in kimenet:
                kimenet+=ch+dictionary[ch][0]
            else:
                kimenet+=ch+dictionary[ch][kimenet.count(ch)]
        print(kimenet)
        print(dictionary)
        print(seged)

    except IndexError:
        print('Letezzen a string')
code_to_dict(valami)

