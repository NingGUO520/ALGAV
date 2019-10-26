def inf(cle1, cle2):
    if isinstance(cle1, int) and isinstance(cle2, int):
        return cle1 < cle2
    elif len(cle1) < len(cle2):

        return True
    elif len(cle1) == len(cle2):
        for i in range(0,len(cle1)):
                
            if cle1[i]<cle2[i]:
            
                return True
            elif cle1[i]>cle2[i]:
                return False
    return False

def eg(cle1,cle2):  

    return cle1 == cle2

