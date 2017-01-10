# Databases and Pseudocode

## Lecture 2 - January 6th, 2017 

**These notes list the main ideas for this lecture. Please check out Alona Fyshe's slides**

---

* Motivating Example:
    * CSC 106 - Keeping Records of Grades
    * Goal: How to work with this Data

* Pseudocode -> Logic writing on your code.
* Algorithm -> Sets of steps

----

**Solution For: The above question**
```
total = 0
count = 0
i = 1

while i =< total # rows in table
    total = total + grade in row i
    count = count + 1
    i = i + 1

average = total / count
```

**Solution For: Keeping track of grades for a specific teacher**
```
total = 0
count = 0 
i = 1

while i =< total # rows in table
    if prof-name of row i = Turing
        total = toal + grade in row i
        count = count + 1
    i = i + 1

average = total / count
```

**Solution For: Inserting a new grade in the table** 

Before:
```
i = # rows in table + 1

stud_id for row i = 313
stud_name for row i = Steve Cook
course_name for row i = CSC 106 (Too much info)
CRN for row i = 23456
prof-name for row i = Turing (Too much info - CRN is all mighty)
grade for row i = 91
```
After:
```
i = # rows in grades table + 1

stud_id for row i = 313
stud_name for row i = Steve Cook
CRN for row i = 23456
grade for row i = 91
```

---

**NOTE:** The question now has two tables to work with instead of one. 

---

**Solution For: Calculating the average for students in class with CRN 23457**
```
total = 0
count = 0
i = 1

while i =< total # of rows in grades tables
    if crn in row i is 23457
        total = total + grade in row i
        count = count + 1
    i + i + 1
average = total / count
```

**Solution For: Calculating a better average**
```
if  count = 0 
    average = 0
else 
    average = total/count
```

**Solution For: Table Case: Inserting a new grade into two tables**
```
if input crn is not in classes table 
    return error
else 
    stud_id for row i = 313
    stud_name = Steve Cook
    crn = 23456
    grade = 91
```

**Solution For: Calculating the average grade for classes that Turing teaches**
```
total = 0 
count = 0
j = 1 (Index into classes table)

while j =< # rows in classes table 
    if row j of classes tables has prof_name = Turing
        my_crn = crn in j of classes table

        i = 1
        while i =< #rows in grades table
            if crn for row i of grades table  = my_crn
                table = total + grade in row i of grades table
                count = count + 1
            i = i + 1
    j = j + 1
```

## Lecture 3 - January 10th, 2017

**Trace Through Code**
Code:
```
Step1 - total=0
Step2 - count=0
Step3 - i=1
Step4 - while i <= # rows in table, repeat steps 5 through 8
Step5 - 	if prof_name of row i equals Turing, do line 6 and 7 
Step6 - 		total = total + grade in row i
Step7 - 		count = count + 1
Step8 -		i=i+1
Step9 - average = total / count
```

Table 1:
| stud_id       | stud_name     | course_name  | crn      | prof_name | grade |
| ------------- |:-------------:| ------------:|---------:|----------:|------:|
| 111           | John Jackson  | CSC 106      | 23456    | Turing    | 45    |
| 200           | Jane McKenzie | CSC 106      | 23457    | Jobs      | 83    |
| 342           | Patricia Dune | CSC 106      | 23456    | Turing    | 94    |
| 301           | Meg Lyon      | CSC 106      | 23457    | Jobs      | 79    |
Note: #rows = 4
Solution:
```
total=0
count=0
i=1

--

total=45
count=1
1=2

--

i=3

--

total=139
count=2
i=4

--

i=5

-- 

Average = 139/2 = 69.5

```

**Write pseudocode that calculates the maximum grade for a student in class with crn = 23456**
**Trace Through Code**
Code:
```
Step1 - max=-1
Step2 - i=1
Step3 - while i <= # rows in table, repeat steps 4 through 7
Step4 - 	if crn of row i equals 23456, do line 5 and 6 
Step5 - 		if max < grade in row i do line 6
Step6 - 			max = grade in row i 
Step7 - 	i=i+1
```

Table:
| stud_id       | stud_name     | course_name  | crn      | prof_name | grade |
| ------------- |:-------------:| ------------:|---------:|----------:|------:|
| 111           | John Jackson  | CSC 106      | 23456    | Turing    | 45    |
| 200           | Jane McKenzie | CSC 106      | 23457    | Jobs      | 83    |
| 342           | Patricia Dune | CSC 106      | 23456    | Turing    | 94    |
| 301           | Meg Lyon      | CSC 106      | 23457    | Jobs      | 79    |

Solution: 
```
max=-1
i=1

--

max=45
i=2

--

i=3

--

max=94
i=4

--

i=5

```

---

## SQL

Sql is a structured query language.

## Database

A database is a collection of tables.

**Install SqLite3**
```bash
brew install sqlite
```

Start by making a blank table: 
```sql
create table grades( stud_id int, stud_name text, course_name text, crn int, prof_name text, grade int);
```

Note: Order of values must match the order of the columns when you created the table.

## Query 

A query is a select statement that tells the computer what columms the result should have. 

Ex. 
```sql
Select stud_name, grade 
from grades;
```

Return
Table 1: Grades
| stud_name	| grade	|
| ---------:| -----:|
| name      | 56    |
| name      | 78    |

Ex. 
```sql
Select avg(grade)
From grades;
```
| avg(grade) |
| ----------:|
| 72.8       |

Ex.
```sql
select max(grade)
from grades;
```
| max |
| ---:|
| 94  |

Ex.
```sql
Select stud_name, grade, crn 
from grades
where crn = 23456;
``` 
| stud_name  | grade   |  crn |
| ----------:| -------:| ----:|
| Joe Smith  |      80 | 23456|
| John Jacks |      45 | 23456|
| Al Green   |	    66 | 23456|
| Greg Black |      60 | 23456|
| Patricia D |      94 | 23456|

Ex. 
```sql
Select stud_name, grade 
from grades
where prof_name = “Jobs”;
```
Note: text must be surrended by quotes. 

| stud_name  | grade|
| ----------:| ----:|
| Meg Lyon   | 79   |
| Jane McKen | 83   |
| Richard Fe | 70   |
| Paul Shelb | 66   |
| John Jacks | 85   |

---

# You should know 
* How to step through pseudocode
* How to write some simple SQL queries using: –  avg
* max
* where
