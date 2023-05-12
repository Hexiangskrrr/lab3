import employee_info as info
import statistics

def test_calculate_average_salary():
    salary = (50000, 60000, 56000, 70000, 65000, 60000)
    result = statistics.mean(salary)
    result = round(result, 2)
    assert(result == 60166.67)

def test_get_employees_by_dept():
    result = info.get_employees_by_dept("Sales")
    expected = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}, {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert(result == expected)

def test_get_employees_by_age_range():
    result = info.get_employees_by_age_range(20,30)
    expected = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000}, {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(result == expected)


