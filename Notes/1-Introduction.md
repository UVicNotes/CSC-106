# CSC 106 - Introduction

## Lecture 1 - January 4th, 2017

* Abacus (Japanese)
* Why should we care about polynomials?
* Analytical Engine
    * Punch Cards (Held Instructions)
    * RAM 
    * CPU
* Tabulate the Census
    * Data Punch Cards
    * IBM
* Computers (Who invented the first computer? A lot of people.)
* Binary 
* Conrad Zuse (Standard - Binary)
* Alan Turing (Crack German Codes - WW2)
* Colossus (Crack German Codes - WW2)
* ENIAC
* Solid State Transistor (Computers No longer for Gov, also for Business) 
* Apple (Bring Computers to Home)
* Macintosh (Desktop and Folders - No longer just a terminal)

## Lecture 2 - January 6th, 2017

Announcements 
*   Alice Gibbons (aligibbo@uvic.ca)
*   Lab Access Cards
*   10$ Access Cards

### Databases and Pseudocode 

* Motivationg Example
    * CSC 106 - Keeping Records of Grades
    * Goal: How to work with this Data

* Pseudocode -> Logic writing on your code.

----

**General Solution**
```
//
total = 0
//
count = 0

// Index
i = 1

while i =< total # rows in table
    total = total + grade in row i
    count = count + 1
    i = i + 1

average = total / count

```

**Only keep track of grades from a specific teacher**
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

**Insert a new grade** 
```
Before:
i = # rows in table + 1

stud_id for row i = 313
stud_name for row i = Steve Cook
course_name for row i = CSC 106 (Too much info)
CRN for row i = 23456
prof-name for row i = Turing (Too much info - CRN is mighty all)
grade for row i = 91

After: 
i = # rows in grades table + 1

stud_id for row i = 313
stud_name for row i = Steve Cook
CRN for row i = 23456
grade for row i = 91
```

---
Added two tables

---

**Average of students in class with CRN 23457**
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

**Better average**
```
if  count = 0 
    average = 0
else 
    average = total/count
```

**Table Case: Insert a new grade**
```
if input crn is not in classes table 
    return error
else 
    stud_id for row i = 313
    stud_name = Steve Cook
    crn = 23456
    grade = 91
```

**Average of grades for classes that turing teaches**
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

---

* Algorithm -> Sets of steps

## Homework 

1. How to write Pseudocode to calculate the average grade different groups of students 
2. Extra practice (try with both one and two-table scenarios):