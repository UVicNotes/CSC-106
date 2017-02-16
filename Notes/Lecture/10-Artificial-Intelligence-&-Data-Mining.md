## Lecture 15 - February 8th, 2017

#### Artificial Intelligence and Data Mining

* Something Fun
    * quickdraw.withgoogle.com/

#### Social Media Data

* 2 million emails per second
* 500 million tweets on twitter a day
* 500 million new videos viewed to youtube a minute. 

#### Scientific Data

* Data collected and stored at enormous speeds (GB/hour)
    * remote sensors on a satellite

**Other Data Sources?**

#### Need for Data Mining

* Human Analysts: Too much work
* Data Mining: automatically discover useful information

**Example:**

* Predict if an email is spam or not
* Train a model
    * Show the computer a bunch of emails, some of which are spam, some of which are not
    * Tell the computer which words appear in each email
    * Computer learns words that tend to appear with spam emails, or with not-spam emails.
* Test the model
    * Show the computer a new email
    * Check if the computer predicts the right class

#### Predictive Data Mining or Supervised learning  

**Learning**

We can think of at least three different problems....

**Ex.** Imagine I'm trying predict wether my neighbour is going to drive into work, so I can ask for a ride. 

* Wether..
    * temp.
    * precipitation
    * day
    * clothes

Memorize vs New Data

| Temp | Precip | Day | Clothes |       |
|------|--------|-----|---------|-------|
| 25   | None   | Sat | Casual  | Walk  |
| -5   | Snow   | Mon | Casual  | Drive |
| 15   | Snow   | Mon | Casual  | Walk  |
| -5   | Snow   | Mon | Casual  |   ?   |

#### Noisy Data

| Temp | Precip | Day | Clothes |       |
|------|--------|-----|---------|-------|
| 25   | None   | Sat | Casual  | Walk  |
| 25   | None   | Sat | Casual  | Walk  |
| 25   | None   | Sat | Casual  | Drive |
| 25   | None   | Sat | Casual  | Drive |
| 25   | None   | Sat | Casual  | Walk  |
| 25   | None   | Sat | Casual  | Walk  |
| 25   | None   | Sat | Casual  | Walk  |
| 25   | None   | Sat | Casual  |   ?   |

Average the data when it's noisy data

#### How can we build a model?

* Decision Tree
    * Predict by splitting on attribute values
    * ID3
        * Normal procedure: top down in a recursive **divide-and-conquer** fashion
        * Process Stops

        
![Decision Tree](../C\)-References/DecisionTree.png)


AI Experience (withGoogle)

* Constructing decision trees (ID3)
    * Normalprocedure:topdowninarecursivedivide-and- conquer fashion
        * First: an attribute is selected for the root node and a branch is created for each possible attribute value
        * Then: the instances are split into subsets (one for each branch extending from the node)
        * Finally: the same procedure is repeated for each branch, using only instances that reach the branch    * Processstopsifallinstanceshavethesameclass   

Attribution Selection:

* Heuristic: Choose the attribute that produces the "purest" nodes
* Entropy of Nodes: Lower the entropy, purer the node

Measuring Purity with Entropy:

* Amount of Information
    * Higher -> messier the group
    * Lower -> purer the group

![Entropy](../C\)-References/Entropy.png)

Bonus:

Trump's Twitter: 

* iPhone Entries (Staff) vs Android Entries (Trump) 
