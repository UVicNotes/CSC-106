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
