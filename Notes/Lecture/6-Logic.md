# Logic 

## Lecture 10 - January 25th, 2017

### Logic

* Logic gates
* Form basis of computer hardware and computer operations
* `OR` Truth Table (+)
* `AND` Truth Table (*)
* Combine : `OR` and `AND`

![Images RefeANdrences](..References/AND&OR.png)

* `Not` (~)

![Images from slides](..References/NOT.png)

### Circuit Diagrams

* Compare for Equality

### Adding with Logic - Full Adder Circuit

* Truth Table -> Set of `OR`, `AND`, and `NOT`
* `XOR` Truth Table (Circle +)

#### Test your understanding

(X and Y) or Z

2nd slide -> E)


### Sorting

* Often useful to have data sorted 
    * find values more quickly
    * test for existence more quickly
* Many algorithms for sorting

### Arrays

* Arrays are like a list
* Start numbering positions at 0
* Square brackets []
* Assign a value to an array

**Note:** Left side changes

* Selection Sort
* Sort hand of cards ?
* Numerically

**Ex.**  [2,8,6,3]

* Unsorted part of the list and sorted part of the list.
* Input integer array my_nums

```
Keep track of sorted array section 
Search through unsorted array for max val
Swap max val with element at the rightmmost position of unsorted section
Move sorted section one element to left
Stop when unsorted section has size 1
```

## Lecture 11 - January 27th, 2017

### Selection Sort

* Find the the largest card, and put it to the rightmost position
* Fin the next largest card, put it in the next-to-rightmost position
* Etc. 

```pseudocode
input integers c(<sub>0</sub>) ... c(<sub>m-1</sub>). m (array)(length)

cur_ind = m-1
while cur_ind > 0
    cur_max = -\infty
    i = 0
    max_ind = 0
    while i <= cur_ind
        if c(i) > cur_max
            cur_max = c(i)
            max_ind = i
        i = i + 1
    swap c(cur_ind) & c(max_ind)
    cur_ind = cur_ind -1
```

**Ex.** Tace through c = [2,1,5,3,4]

```
m=5
cur_ind = 4
cur_max = -\infty
i=0
max_ind = 0

cur_max = 2
i = 1 

i = 2

cur_max = 5
max_ind = 2
i = 3

i = 4

cur_ind = 4
i = 5

cur_ind = 3

cur_max = -\infty
i = 0
max_ind = 0

cur_max = 2
cur_ind = 0
i = 1

i = 2

ect.
```

### Bubble Sort 

* Start at the begining of the array 
* Consider the first two numbers (position 0&1)
    * If they are out of order, swap them
* Consider the next two numbers (position 1&2)
    * If they are out of order, swap them
* Continue comparing consecutive numbers and swapping until you reach the end of the array
* Start over at the begining of the array 
* Continue until you make it through the whole array wthout doing any swaps

```pseudocode
input integers c(<sub>0</sub>) ... c(<sub>m-1</sub>), m (array)(length)

swapped = True
while swapped is True
    swapped = False
    i = 1
    while 1 <= m-1
        if c(i-1) > c(i)
            swap c(i-1) & c(i)
            swapped = true
        i = i + 1
```   

#### Practice

Converting Pseudocode to Flowcharts **Important**
