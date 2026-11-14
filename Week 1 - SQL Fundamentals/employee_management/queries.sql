-- Query 1: Display all employees

SELECT *
FROM employees;

-- Query 2: Employees earning more than 1000

SELECT name, department, salary
FROM employees
WHERE salary > 1000
ORDER BY salary DESC;

-- Query 3: Department salary report

SELECT
    department,
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY total_salary DESC;
