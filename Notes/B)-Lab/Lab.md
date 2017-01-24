## Databases

### Lab 1 - January 10th, 2017

#### SqLite

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
 
#### Aggregate function

* count
* max
* min
* avg

### Lab 2 - January 17th, 2017

#### Flowcharts

* Rounded Rectangle -> Start and Stop
* Rectangle -> Process
* Diamond -> Decision
	* Yes or No
* Italic Rectangle -> Data Input or Output

##### Communicate an algorithm 

* Easy 
* Visual
* Simple for hard problems

##### Criteria for lab assignment 

* Flowchart: 
    * Draw by hand **or** 
    * Draw with https://draw.io

##### You should know how to: 

* Convert Pseudocode to Flowchart and Flowchart to Pseudocode

**Lab Exercise: Draw a flowchart for playing 1 turn of "computer pictionary"**

* 2 teams (Team A and B)
* Only using names of movies
* Computer draws movie name (if it can)
* 5 guesses

N.B. Team A draws a name -> Team A inputs name into computer -> Team B guesses (Max. 5 times)

**My Solution:**

![My Solution](../C\)-References/lab2_mySolution.png)

**Group Solution:**

![My Solution](../C\)-References/lab2_solution.png)


Ex. 

**PseudoCode Exercise - Get the name and title of books where there is a 1 and the year in lesser than 1960**


| name     | title    | year | human |
| --------:| --------:| ----:| -----:|
| example  | example  | 1983 | 1     |
| example2 | example2 | 1924 | 0     |
| example3 | example3 | 1999 | 1     |

Answer: 

Select name, title from characters where human=1 and year<1960