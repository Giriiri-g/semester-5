-- 1. Display the name of the employee who earns the highest salary
SELECT ename FROM Employee
WHERE sal = (SELECT MAX(sal) FROM Employee);

-- 2. Display the employee number and name for employee working as clerk and earning highest salary among clerks
SELECT eno, ename FROM Employee
WHERE job = 'clerk' AND sal = (SELECT MAX(sal) FROM Employee WHERE job = 'clerk');

-- 3. Display the names of salesmen who earn a salary more than the highest salary of any clerk
SELECT ename FROM Employee
WHERE job = 'salesman' AND sal > (SELECT MAX(sal) FROM Employee WHERE job = 'clerk');

-- 4. Display the names of clerks who earn a salary more than the lowest salary of any salesman
SELECT ename FROM Employee
WHERE job = 'clerk' AND sal > (SELECT MIN(sal) FROM Employee WHERE job = 'salesman');

-- 5. Display the names of employees who earn a salary more than that of Jones or greater than that of Scott
SELECT ename FROM Employee
WHERE sal > (SELECT sal FROM Employee WHERE ename = 'Jones')
   OR sal > (SELECT sal FROM Employee WHERE ename = 'Scott');

-- 6. Display the names of the employees who earn the highest salary in their respective departments
SELECT ename FROM Employee
WHERE sal = (SELECT MAX(sal) FROM Employee WHERE dno = Employee.dno);

-- 7. Display the names of the employees who earn the highest salaries in their respective job groups
SELECT ename FROM Employee
WHERE sal = (SELECT MAX(sal) FROM Employee WHERE job = Employee.job);

-- 8. Display the employee names who are working in the accounting department
SELECT ename FROM Employee
WHERE dno = (SELECT dept_no FROM Department WHERE dname = 'accounting');

-- 9. Display the employee names who are working in Chicago
SELECT ename FROM Employee
WHERE dno = (SELECT dept_no FROM Department WHERE location = 'Chicago');

-- 10. Display the job groups having total salary greater than the maximum salary for managers
SELECT job FROM Employee GROUP BY job
HAVING SUM(sal) > (SELECT MAX(sal) FROM Employee WHERE job = 'manager');

-- 11. Display the names of employees from department number 10 with salary greater than any employee in other departments
SELECT ename FROM Employee
WHERE dno = 10 AND sal > (SELECT MAX(sal) FROM Employee WHERE dno <> 10);

-- 12. Display the names of the employees from department number 10 with salary greater than that of all employees working in other departments
SELECT ename FROM Employee
WHERE dno = 10 AND sal > ALL (SELECT sal FROM Employee WHERE dno <> 10);
