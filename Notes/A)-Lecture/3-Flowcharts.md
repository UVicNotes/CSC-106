# Flowcharts

## Lecture 5 - January 13th, 2017

**Notes Missing**

Contribute your notes [here](https://github.com/UVicNotes/CSC-106)!

---

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