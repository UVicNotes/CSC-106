# Flowcharts

## Lecture 5 - January 13th, 2017

**Notes provide by a kind classmate :D**

### Algorithms and Flowcharts

* Rectangle -> Process 
* Rhombus -> Data (Input of Output)
* Diamond -> Decision 
* Rounded Rectanlge -> Start and Stop

**Ex.** Making a flowchart for collatz conjecture 

![Flowchart1](../C\)-References/Flowcharts_Figure1.jpg)

**Ex.** A flowchart to calculate avg. of grades of student of Turing

![Flowchart2](../C\)-References/Flowcharts_Figure2.png)

**Ex.** To print a phone number corresponding to given name or else print "no such name"

![Flowchart3](../C\)-References/Flowcharts_Figure3.png)

## Lecture 6 - January 17th, 2017

**Modulo:** The ramainder after dividing. 

**Question:** Determine if a year is a leap year

```pseudocode
Step1 	Input integer year
Step2 	if year modulo 4 is 0 do Step3-9
Step3		if year modulo 100 is 0 do Step4-7
Step4			if year modulo 400 is 0 do Step5
Step5 				is_leap_year=True
Step6			else do Step7
Step7 				is_leap_year=False
Step8 		else do Step9
Step9			is_leap_year=True
Step10	 else do Step11
Step11 		is_year_leap=False
Step12 	 return is_leap_year
```