import employee_info as info
import statistics

def test_calculate_average_salary():
    salary = (50000, 60000, 56000, 70000, 65000, 60000)
    result = statistics.mean(salary)
    result = round(result, 2)
    assert(result == 60166.67)

def test_get_employees_by_dept():
    result = info.get_employees_by_dept("Sales")
    assert(result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}, {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}])


