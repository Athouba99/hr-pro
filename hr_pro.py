class Employee:  #class 1
   #Employee class here
    def __init__(self,name,age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def get_annual_salary(self,salary):
        return salary*12 

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}, Salary:{self.salary}, Working years:{self.employment_years}"
      
class Manager(Employee): #class 2 
    #Manager class here
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name,age, salary, employment_years)
        self.name = name 
        self.age = age
        self.salary = salary
        self.employment_years = employment_years 
        self.bonus_percentage = bonus_percentage 

    def get_bonus(self, bonus_percentage):
        return bonus_percentage*12

    def __str__(self):
      return f"Name:{self.name}, Age:{self.age}, Salary:{self.salary}, Working Years:{self.employment_years}, Bonus:{self.bonus_percentage}"  
  
def main():
	# main code here
    list1 = [] # empty lilst to be filled 
    list1.append(Employee ("laila",24 , 9999, 4))
    list1.append(Employee("Moh", 27, 999, 2))
    #list1.append(Employee("shosho", 24, 666, 1))
    
    for obj in list1:
        print(obj.name, obj.age, obj.salary, obj.employment_years)

    list2 = []
    list2.append(Manager("sammy", 52, 4600, 19, 1380))
    for obj in list2:
        print(obj.name, obj.age, obj.salary, obj.employment_years, obj.bonus_percentage)

if __name__ == '__main__':
	main()
