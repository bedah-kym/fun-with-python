
marks=[5,25,43,88,81,72]

def gradestudents(marks):
    finalgrade=[]
    if 0<= marks[0] <=60:
        for x in range(1,(marks[0]+1)):
            if marks[x] < 38:
                finalgrade.append(marks[x])
            else:
                multiple=marks[x]
                while multiple %5 != 0:
                    multiple+=1
                #print('multiple =',multiple,'-',marks[x])
                if multiple - marks[x] <3:
                    finalgrade.append(multiple)
                elif multiple - marks[x] ==3:
                    finalgrade.append(marks[x])
                else:
                    finalgrade.append(marks[x])
        #print(finalgrade)
        return finalgrade
                    


print(gradestudents(marks))

print('a'+'b')
