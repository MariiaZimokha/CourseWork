select * from Employees 
where EmployeeID = 8;
# 2 
select FirstName,LastName
	from Employees where City = "London";
#3
#16
select FirstName,LastName 
	from Orders left join Employees 
	on Orders.EmployeeID = Employees.EmployeeID
	where year( Orders.ShippedDate) > 1996 
	AND year( Orders.ShippedDate) < 1998
	group by Employees.FirstName;
#17
select count(OrderID)
	from Orders join Customers 
	on Orders.CustomerID = Customers.CustomerID
	where Customers.Country = "France";
#18
select CustomerID, ContactName
	from  Customers 	
	group by ContactName
	having Country = "France"
	and CustomerID in 
	( select CustomerID from Orders) >= 1 ;
#19
select CustomerID, ContactName
	from  Customers 
	having Country = "France"
	and CustomerID in 
	( select CustomerID from Orders) >= 1 ;
#20
select CustomerID, ContactName
	from  Customers 
	#group by ContactName 
	where Country = "France"
	and CustomerID in 
		(select CustomerID from Orders 
		where OrderID in 
			(select  OrderID from Order_Details 
			where ProductID in 
				(select ProductID from Products
				where ProductName = "Tofu")))
	;
#21

	
	