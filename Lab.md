# Databases

## Lab 1 - January 10th, 2017

**SqLite**

How we access data is we use these things called queries. 

In the terminal type in:

```bash
sqlite3

and then

.read FILENAME

and then

select * from characters;

```

Order matters when running *select* in the terminal from the database. 

It is not case sensitive.

Ex. You can use FROM, ChaRacters, Select, ect. 

**Select dinstinct:** applies only to what follows, and makes it so only unique data gets return. 
 
 Ex.
 
 ```sql
 select distinct title from characters;
 ``` 
 
 
You can have an or in your where.

Ex. 

```sql
 select * from characters where title = 'Horton Hears a Who' or title = 'Horton Hatches the Egg';
 ```
 
 You can order your return.
 
 Ex. 
 
 ```sql
 select name, year from characters order by year, title;
 ```
 
**Aggregate function**

* count
* max
* min
* avg

