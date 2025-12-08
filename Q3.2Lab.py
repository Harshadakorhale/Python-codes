# 2. Create a class Employee with method calculate_salary() that takes basic pay and 
# calculates total salary with 10% bonus. Test with basic = 40000.

class Employee:
    def calculate_salary(self,basic_pay):
        bonus = basic_pay*0.10
        total_salary = bonus+basic_pay
        return total_salary
    
emp = Employee()
basic = 40000
print(emp.calculate_salary(basic))