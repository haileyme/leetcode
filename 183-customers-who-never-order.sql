select distinct Name "Customers" from customers, orders where customers.Id not in (select CustomerID from orders);
