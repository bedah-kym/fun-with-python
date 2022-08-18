class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
 
    @staticmethod
    def validate(num1,num2):
        if (num1 + num2 ) < 0:
            return ("brooo fuck off")
        else:
            return num1+num2

    def combine(self):
        print (self.fname,self.lname)
        
    @classmethod
    def fullname(cls,full):
        return cls(full,full)

    


print(Employee.fullname('beda').combine())
e2 = Employee('kim','yo')
#print(Employee.validate(7,2))
print(e2.combine())
#print(e2.combine)

#print(e.validate())
    
#hi furture me i left this code with  a bug coz i know ur dumb ass already forgot this shit
# fix it without sololearn or google 
