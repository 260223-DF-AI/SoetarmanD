CREATE DATABASE sql_practice;

CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'Building A', 500000),
('Sales', 'Building B', 300000),
('Marketing', 'Building C', 200000),
('HR', 'Building D', 150000);

INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id) VALUES
('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('Website Redesign', '2024-01-01', '2024-06-30', 50000, 3),
('Mobile App', '2024-02-15', '2024-12-31', 150000, 1),
('Sales Portal', '2024-03-01', '2024-09-30', 75000, 2),
('HR System', '2024-04-01', '2024-08-31', 40000, 4);

SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;

ALTER TABLE employees ADD COLUMN phone VARCHAR(20);

ALTER TABLE departments ALTER COLUMN budget TYPE DECIMAL(15, 2);

CREATE TABLE training_courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_hours INT,
    instructor VARCHAR(100)
);

INSERT INTO employees (first_name, last_name, email, salary) VALUES
('Grace', 'Lee', 'grace.lee@company.com', 58000),
('Ivan', 'Chen', 'ivan@company.com', 61000),
('Julia', 'Kim', 'julia@company.com', 55000);

-- A) Give all Engineering department employees a 10% raise:
UPDATE employees SET salary = salary + (salary * 0.1) WHERE dept_id = 1;

-- B) Update Bob Smith's email to <bob.smith@company.com>:
UPDATE employees SET email = 'bob.smith@company.com' WHERE first_name = 'Bob';

-- A) Delete all projects that have already ended (end_date before today):
DELETE FROM projects WHERE end_date < CURRENT_DATE;

-- B) **CAREFUL!** Write (but don't run) a DELETE that would remove all employees without a department. What makes this dangerous?
DELETE FROM employees WHERE dept_id IS NULL;

-- **Query 3.1:** List all employees ordered by salary (highest first)
SELECT * FROM employees
ORDER BY salary DESC;

-- **Query 3.2:** Find all employees in the Engineering department
SELECT * FROM employees
WHERE dept_id = 1;

-- **Query 3.3:** List employees hired in 2021 or later
SELECT * FROM employees
WHERE hire_date > '2021-01-01'

-- **Query 3.4:** Find employees with salary between 60000 and 80000
SELECT * FROM employees
WHERE salary > 60000 and salary < 80000

-- **Query 3.5:** Find employees whose email contains 'company'
SELECT * FROM employees
WHERE email LIKE '%company%';

-- **Query 3.6:** List departments in Buildings A or B
SELECT * FROM departments
WHERE location = 'Building A' or location = 'Building B';

-- **Query 3.7:** Calculate the total salary expense per department
SELECT SUM(salary) as salary_expense, dept_id FROM employees
GROUP BY dept_id;

-- **Query 3.8:** Find the average, minimum, and maximum salary
SELECT AVG(salary), MIN(salary), MAX(salary) FROM employees;

-- **Query 3.9:** Count employees in each department, only show departments with 2+ employees
SELECT dept_id
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2;

-- **Query 3.10:** Create a report showing full name (first + last), department name, and formatted salary
SELECT employees.first_name, employees.last_name, departments.dept_name, employees.salary
FROM employees
JOIN departments on employees.dept_id = departments.dept_id;

-- Find employees who earn more than the average salary.
SELECT *
FROM employees
WHERE salary > (SELECT (AVG(salary)) FROM employees);

-- List departments that have at least one project.


-- Find the employee with the highest salary in each department.
SELECT dept_id, MAX(salary)
FROM employees
GROUP BY dept_id


-- Calculate how long each employee has been with the company (in years and months).
