#this is the solve for turing basketball question with strange rules
def calPoints(ops)-> int:
    results = []
    sum = 0
    for char in ops :
        l= len(results)
    
        if type(char) == int:
            results.append(char)
        
        elif char == 'D': 
            new = ops[l-1]*2
            results.append(new)
        
        elif char == '+': 
            new = results[l-1]+results[l-2]
            results.append(new)
        
        elif char == 'C': 
            results = results[:-1]
            
        else:
            print('invalid record')
            break
        

    for char in results:
        sum += char

    return sum
            
            
ops = [5,2,'C','D','+']

print('sum =',calPoints(ops))


