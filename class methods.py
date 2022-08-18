class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
 
    @staticmethod
    def validate(current_year,birth_year):
        age=current_year - birth_year
        if age < 18:
            return ("brooo fuck off")
        else:
            print(f'you are {age} years which is legal')

    def combine(self):
        print (self.fname,self.lname)
        
    @classmethod
    def fullname(cls,full):
        return cls(full,full)

    


print(Employee.fullname('beda').combine())
e2 = Employee('kim','yo')
print(Employee.validate(2022,1999))
print(e2.combine())

    
#hi furture me i left this code with  a bug coz i know ur dumb ass already forgot this shit
# fix it without sololearn or google 
