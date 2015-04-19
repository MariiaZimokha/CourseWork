
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
	where Country = "France"
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
<<<<<<< HEAD
select * from Customers;
=======



select 
	e.FirstName,
	e.LastName,
	floor(datediff(now(),e.BirthDate) / 365.25) as Age

from Employees as e
where floor(datediff(now(),e.BirthDate) / 365.25) > 55;	
	
#6
select 
	max(floor(datediff(now(),e.BirthDate) / 365.25)) as MaxAge,
	min(floor(datediff(now(),e.BirthDate) / 365.25)) as MinAge,
	avg(floor(datediff(now(),e.BirthDate) / 365.25)) as AVGAge
	from Employees as e
	where e.City = "London";

#7
select 
	e.City,
	max(floor(datediff(now(),e.BirthDate) / 365.25)) as MaxAge,
	min(floor(datediff(now(),e.BirthDate) / 365.25)) as MinAge,
	avg(floor(datediff(now(),e.BirthDate) / 365.25)) as AVGAge
	from Employees as e
	group by e.City;
#8
select 
	e.City,
	max(floor(datediff(now(),e.BirthDate) / 365.25)) as MaxAge,
	min(floor(datediff(now(),e.BirthDate) / 365.25)) as MinAge,
	avg(floor(datediff(now(),e.BirthDate) / 365.25)) as AVGAge
	from Employees as e
	group by e.City
	having AVGAge >60;
#21
select 
	c.CompanyName,
	#o.OrderDate,
	sum( d.Quantity * d.UnitPrice),
	sum( d.Quantity) Total
	#p.ProductName
	from Customers c
	join Orders  o 
		on c.CustomerID = o.CustomerID	
	join Order_Details d
		on o.OrderID = d.OrderID
	join Products p
		on d.ProductID = p.ProductID
where p.ProductName = 'Tofu'
group by c.CompanyName
;

#22
select 
	c.ContactName,
	c.Country,
	o.OrderID,
	p.ProductName,
	s.Country
	from Customers c
	join Orders  o 
		on c.CustomerID = o.CustomerID	
	  join Order_Details d
		on o.OrderID = d.OrderID
	 join Products p
		on d.ProductID = p.ProductID
	join  Suppliers s
		on p.SupplierID = s.SupplierID
	where c.Country = "France"
	and s.Country != "France"
	order by s.Country;
#23
#24
select 
	c.ContactName,
	c.Country,
	o.OrderID,
	p.ProductName,
	s.Country
	from Customers c
	join Orders  o 
		on c.CustomerID = o.CustomerID	
	  join Order_Details d
		on o.OrderID = d.OrderID
	 join Products p
		on d.ProductID = p.ProductID
	join  Suppliers s
		on p.SupplierID = s.SupplierID
	where c.Country = "France"
	and s.Country = "France"
	order by s.Country;

#25
select 
	c.Country,
	o.OrderID,
	d.Quantity as quantity,
	sum(d.Quantity) as Quantity
	from Customers c
	join Orders  o 
		on c.CustomerID = o.CustomerID	
	join Order_Details d
			on o.OrderID = d.OrderID
	group by c.Country
;
#26
select 
	c.Country,
	sum(CASE WHEN c.Country = s.Country THEN d.Quantity END) domestic,
	sum(CASE WHEN c.Country != s.Country THEN d.Quantity END) nondomestic
	#s.Country
	#(select s.Country from s  ) domestic
	from Customers c
	join Orders  o 
		on c.CustomerID = o.CustomerID	
	join Order_Details d
		on o.OrderID = d.OrderID
	 join Products p
		on d.ProductID = p.ProductID
	join  Suppliers s
		on p.SupplierID = s.SupplierID
	#where c.Country= s.Country
	#order by c.Country ,s.Country
	group by  c.Country
	#having s.Country = c.Country and s.Country != c.Country
	
