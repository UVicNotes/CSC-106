## Lecture 29 - March 28th, 2017

### Guest Lecture
by Dr. Frank Ruskey

#### Problems you can't compute 

**Theoritical Computer Science**

#### Decidable or undecidable?

There is indeed some undecidable problems/questions

**Example:** The 50$ is not in the envelop

* --> True
* --> False (After putting the money in the envelop)

##### TRUE or FALSE

* Exactly one of (A), (B) is TRUE
* Someone in CSC 106 will not get an A+ 

##### TRUE or FALSE or neither

--

#### Classification of words

**Auto Logical (Apply to themselves)** 

* Short
* Undersandable 
* Polycyllble 
* English 

or 

**Heterological (Do not apply to themselves)**

* Long
* Abstract
* Monosyllabic
* French


Q: Is heterological heterological?

* A: If yes then no
* A: If no then yes
* A: Set still sets ...

AGA?

In lisp <- no distinction betwween programs & data

```LISP
heterological(p) := ¬p(p)
hetero(hetero) = ¬hetero(hetero)
               = ¬ ¬hetero(hetero)
               = ¬hetero(hetero)

---

terminates(f, x)
f-program, x-data
    returns True or False (true only if f terminates on data x)

---

hetero(f) := if terminates(f, f)
                then ¬ f(f)
---

hetero(hetero) = ¬hetero(hetero) (contradiction)

---

==> (implies) Terminates does not exist
```

"halting probem" - alan turring

#### Undecidable problems
* The halting (terminates)
* Does a program contain a virus?
* Diophantine equation solving (hilberts 10th problem)
* Tiling the plane with square tiles 
* Snake problem
* Life
* Virus detection is an undecidable problem

--

#### Golly -> Life Game (Source Forge)

* Glider -> they fly away
* Allow us to make a computer
* Glider Gun
* Does a life configuration terminate? (cycling state)

[Life in Life Youtube Video (1:29)](https://www.youtube.com/watch?v=xP5-iIeKXE8)
