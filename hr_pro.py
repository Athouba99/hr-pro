class Employee:  #class 1
   #Employee class here
    def __init__(self,name,age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def get_annual_salary(self,salary):
        return salary*12 

      
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
        

        
        
def main():
	# main code here

if __name__ == '__main__':
	main()
