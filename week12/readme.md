# Week 12 Relational Database (SQL) 


## Using SQLite with Python
- see files 
```
sqlite_example.py
sqlite_example2.py
sqlite_example3.py
```


## Joining Tables
### Ref: https://www.diffen.com/difference/Inner_Join_vs_Outer_Join
### There are two types of joins
- Inner Join
- Outer Join
  - Left Outer Join (or Left Join)
    - Right Outer Join (or Right Join)
    - Full Outer Join (or Full Join) 
- Example in join_example_database.db

#### Inner Join

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices INNER JOIN Quantities
ON Prices.Product = Quantities.Product;

```

#### Left Join

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices LEFT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

#### Right Join -- Doesn't work in SQLITE3

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices RIGHT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

#### Left Join -- This works

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Quantities LEFT OUTER JOIN Prices
ON Quantities.Product = Prices.Product;
```

#### Full Outer join -- does not work

```sql
SELECT Prices.Product, Prices.Price, Quantities.Quantity
FROM Prices FULL OUTER JOIN Quantities
ON Prices.Product = Quantities.Product;
```

### Emulate Full outer join
- REF: https://www.sqlitetutorial.net/sqlite-full-outer-join/

```sql
SELECT Prices.Product, Prices.Price,  Quantities.Product, Quantities.Quantity
FROM Prices 
LEFT OUTER JOIN Quantities
ON Prices.Product = Quantities.Product
UNION ALL
SELECT Prices.Product, Prices.Price, Quantities.Product, Quantities.Quantity
FROM Quantities 
LEFT OUTER JOIN Prices
ON Quantities.Product = Prices.Product;
```



## Database Review and Normalization

- Why use a database?
  - Ref: https://www.bbc.co.uk/bitesize/guides/z8yg87h/revision/4
  - Data is stored efficiently; saves space
  - Because data is stored efficiently, you can access it faster; easy to search
  - Because data is stored efficiently, you can easily update and remove data
  - Easily sort and group data
- What is database normalization?
  - Ref: https://www.complexsql.com/database-normalization/
  - Ref: http://www.databasedev.co.uk/1norm_form.html
  - The purpose of database normalization is to:
    - eliminate redundant data
    - reduce complexity of data, making it easier to manage the data and make change
    - ensure logical data dependencies
- How is database normalization achieved?
  - By fulfilling five normal forms. Each normal form represents an increasingly stringent set of rules. Usually fulfilling the first three normal forms is sufficient.
  - Ref: https://www.1keydata.com/database-normalization/first-normal-form-1nf.php
- First Normal Form  (1NF): 
  1. if there are no repeating groups.
  2. all values are atomic, meaning they are the smallest meaningful value
- Second Normal Form  (2NF): 
  1. the table is in first normal form
  2. each non-key field is functionally dependent on the entire primary key
- Third Normal Form (3NF):
  1. the table is in second normal form
  2. there are no transitive dependencies

- Problems with example1
  - Repeating group of fields
  - The project and time fields are not made up of atomic values
  - Can't sort by last name
  - Can't sort by time because field is type text
  - Assumed relationship between project and time

- Analysis of example2
  - Can sort now!
  - How can you add another project?


- Analysis of example3 -- first normal form
  - Can do groups by employeeid or projectnum
  - Can sort by time
  - Can sort by name

- Analysis of example4
  - How would you update the project title for a given project? Have to edit in many places
  - Can you add a project without an employeeid?
  - How can you delete a project?

- Analysis of example5
  - second normal form

- Analysis of example 6
  - Phone number, which is a non-key field, has transitive dependency on another non-key field. 

- Analysis of example7
  - Removed transitive dependency 


## Example5 in Python
- How do you recreate the tables in python?
  - Write utility functions
    - A connection function
    - A create table function
    - A select function
    - Some insert functions