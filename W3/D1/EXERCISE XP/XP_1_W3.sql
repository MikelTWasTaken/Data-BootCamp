Create Table Items(
Item_name VARCHAR(100) Not Null, 
Price INT Not Null
);

Create Table Customers(
First_name VARCHAR (100) Not Null,
Last_name VARCHAR (100) Not Null
);

Insert Into Items (Item_name, Price)
VALUES ('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

Insert Into Customers(first_name,Last_name)
VALUES('Greg', 'Jones'),
('Sandra','Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');