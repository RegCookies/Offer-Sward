# Write your MySQL query statement below
SELECT D.Name as Department, E.Salary as Salary,E.name as Employee
from Employee E,Department D 
where E.DepartmentId = D.Id and
(Select count(distinct Salary) From Employee where DepartmentId=D.Id and Salary>E.Salary)<3
