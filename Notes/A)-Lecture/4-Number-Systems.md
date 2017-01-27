# Binary / Hex / 2s Complement


### Lecture 4 - January 17th, 2017

#### Why Binary?

* Binary is how computers talk
	* to themselves **AND**
	* to each other


#### Decimal Numbers

**A binary abacus** -> [Example](hdp://www.advanced-ict.info/mathemaAcs/abacus.html)

Ex. 101 is 5 in binary

| 1  | 0  | 1  |
| --:| --:| --:|
| 2^2| 2^1| 2^0|

$$

1x2^2 + 0x2^1 + 1x2^0

1x4 + 0x2 + 1x1 = 5

$$

![Binary Number Example](/Users/dominiquecharlebois/Desktop/Reference_Binary.png)

**NOTE:** Test Material

Ex. What is 11111 in decimal number?

Answer: 31

Ex. What is the highest number you can encode with n bits?

Answer: 2^n -1

#### Encode Numbers

**Note:** If the decimal number is a perfect power of two, it will be easy to find, but if it's not you have **two methods**. 

##### Method 1

$$

5 = 4 + 1

So 2^2 and 2^0

So 00101 = 5

$$

##### Method 2

```Pseudocode
Step1   input: number_in cur_number = number_in binary_string = “”
Step2   while cur_number >= 2
Step3       my_encoding = input%2
Step4       add my_encoding to leW side of binary string 
Step5       cur_number = round_down(cur_number/2)
Step6   add cur_number to leW side of binary string
```

Ex. What is 11 in binary?

```
num_in = 11

binary_string=""
11%2 = 1

binary_string="1"

11/2 = 5.5 -> 5
5%2 = 1

binary_string="11"

5/2 = 2.5 -> 2
2%2 = 0

binary_string="011"

2/2 = 1

binary_string="1011"
```

Ex. What is 8 in binary?  

```
num_in = 8 

binary_string=""
8%2 = 0

binary_string="0"

8/2 = 4
4%2 = 0

binary_string="00"

4/2 = 2
2%2 = 0

binary_string="000"

2/1 = 1

binary_string="1000"
```

**NOTE:** Practice on your own. 




### Lecture 5 - January 18th, 2017

Helper: Question 2 - Assignment 1 

* Input for this program is a list of numbers. 
* Pseudo code for addition. 

```
a(m-1), a(m-2), a(1), a(0)
```

| 4      | 3      | 7    |
| ------:| ------:| ----:|
| a(m-1) | a(m-2) | a(0) |

Answer: m=3

| 3   | 2    | 9    |
| ---:| ----:| ----:|
|b(2) | b(1) | b(0) |

```
437+329=766
```

#### Draw a flow chart

    * Use draw.io
    * Export as an image
    * Hand in PDF


#### Binary Numbers

10110 = 22
01001 = 9

**Tip:** If it ends with a 1 it is odd. If it ends in a 0 it is even.

8 -> 01000
5 -> 00101

#### Algorithm Decimal Number - Binary. 

Ex. Binary Conversion

```
binary_string=""

23%2 = 1

binary_string=1

23/2 = 11.5 -> 11
11%2 = 1

binary_string=11

11/2 = 5.5 > 5
5%2=1

binary_string=111

5/2=2.5 -> 2
2%2=0

binary_string=0111

2/2 = 1

binary_string=10111
```

**Note:** If a question ask for 5 bit number, you must include 5 places.

#### Adding Binary Numbers

Ex. 00111+00001=01000

|     |     |  1  |  1  |  1  |     |
| ---:| ---:| ---:| ---:| ---:| ---:|
|     |  0  |  0  |  1  |  1  |  1  |
|  +  |     |     |     |     |     |
|     |  0  |  0  |  0  |  0  |  1  |
|  =  |     |     |     |     |     |
|     |  0  |  1  |  0  |  0  |  0  |

Bonus: 00111+00111=01110

|     |     |  1  |  1  |  1  |     |
| ---:| ---:| ---:| ---:| ---:| ---:|
|     |  0  |  0  |  1  |  1  |  1  |
|  +  |     |     |     |     |     |
|     |  0  |  0  |  1  |  1  |  1  |
|  =  |     |     |     |     |     |
|     |  0  |  1  |  1  |  1  |  0  |
 
 
#### Encoding Negative Numbers

1. Encode the positive number
2. Flip all the bits (1->0 and 0->1)
3. Add 1 to the new bit string
 
Ex. Convert -9 into binary

```
01001
10110
10111
```
 
Ex. Convert 12 into binary

```
01100
10011
10100
```
 
#### Two's complement number
 
**NOTE:** Unsigned Binary Number or a Two's Complement Number. 

**Ignore overflow that carries in Two's compliment**

#### Convert Two's complement into decimal

1. If negative: 
    * Flip a bit and add one
    * Put the negative back at the end
2. If positive: 

## Lecture - January 20th, 2017

### Lecture 6 - January 24th, 2017

#### Guest Lecture 
Dy George Tzanetakis (Associate Professor)

Music and Computer Science

[The Northways](https://vimeo.com/147538529)

[Northway Games](http://northwaygames.com)

**Human Computer Interaction**

1. Lack of shared understanding
2. Communication Bottleneck:
    * Input: Mouse/Keyboard (touch screen)
    * Output: Rectangle 2D screen, speakers


**Why Music**

The way music is **created**, **distrubuted**, and **perceived** had been and will be transformed by advances in technology.

Arguably the most complex and expressive interaction with artifacts.

**Digital Music Data**

2000: ~1000 tracks

2010: ~13 million tracks

**Statisticaly Supervised Learning**

**Playing/Improvising music with a computer**

Machine Orchestr Kapur - Jan. 2010

---

End of material for Midterm 1

---
