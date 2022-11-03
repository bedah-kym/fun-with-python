string = '[]{}'

def isValid(s: str)->bool:
    control = ['(',')','{','}','[',']',]
    control2 = {
        '(':')',
        '{':'}',
        '[':']'
        }
    
    result = None
    
    for char in s :
        try:
            if char in control:
                opp = control2[char]   
                if opp in s :
                    result = True
                else:
                    result = False
                    break
            else:
                result = False
                break
            
        except KeyError:
            continue
        

    return result



print(isValid(string))
