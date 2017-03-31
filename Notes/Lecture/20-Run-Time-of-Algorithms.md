## Lecture 26 - March 21st, 2017

### Run time of algorithms

#### Searching a Tree

* Compare these algorithms 
    * DFS
    * BFS
    * Pre-order traversal
    * Post-order traversal
    
* In pre/post order traversal, "visit" means add the node to the result.

 
#### Analyzing Algorithms

* Problems have many solutions
    * Which solution is the best?
* The best car:
    * Ease of hadling
    * Style
    * Fuel Efficiency 
* Which sorting is best?
    * [Toptal](www.toptal.com/developers/sorting/algorithms)

#### Attributes of Algorithms

The best algorithm:

1. Ease of Understanding by Humans
2. Time/Space Efficient
3. Elegance
4. Correctness
    5. Is the problem specified correctly
    6. Does the algorithm produce the correct result?

##### Efficiency: An algorithm's use of time and space resources

* Timing an algorithm is not always useful
* Confounding factors: machine speed, soze of input
* We analyze instead based on the number of operations. 
    
##### Benchmarking: timing an algorithm on standard data sets

* Testing hardware and operating system, etc.
* Testing real-world performance limits. 
    
##### Example: Searching find a value in an array, or return that its not there

##### Sequential Search Algorithm 

**Order of magnitude - order n**

| f(x) | = | cx | 
|-----:|---|---:|
| n    |   |  n |

## Lecture 28 - March 24th, 2017

* "order" n^2 

#### When Things Get Out of Hand

**Polynomially bounded:** an algorithm that does work on the order of 

##### Hamiltonian circuit -> lenghtN

* Brute Force
* Graph -> Build a Tree

##### intractable:

* Hamiltonian circuit
* Traveling salesperson
* Bin packing
* Chess
    
We find an approximation algorithm to deal with this problem ^^

#### Space (Memory) Efficiency

* Time and space are often traded off
    * With enough space, we can do search in constant time!!

#### Summary: 

* How can we compare algoritms?
    * Multiple dimensionss
        * Some easier to measure than others
* Efficiency
    * Time and space
* Time effiency

#### Page Rank

* PageRank -> 2 People (Founders of Google)

--

* Webpage -> node
* Edge -> link

