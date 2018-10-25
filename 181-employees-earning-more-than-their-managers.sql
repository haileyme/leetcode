select a.Name "Employee" from Employee a, Employee b where a.ManagerID = b.Id and a.Salary > b.Salary
