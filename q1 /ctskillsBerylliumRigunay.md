> Annex B
> 
> Computational Thinking Exercise: "Smart Vending Machine"
> 
> Section: 9-Beryllium Score:____________
> 
> C# / Name: Ethan Paul P. Rigunay Date: 8/14/2026
> 
> Scenario
> Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:
> 
> Sometimes the machine does not give the correct change.
> Items run out, but the machine doesn’t notify anyone.
> Students press the wrong buttons and get the wrong item.
> The machine is slow when multiple students use it in succession.
> Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

# **Step 1: Identify the Big Problem**
**Main Problem:** The vending machine frequently malfunctions by dispensing the wrong change, items run out without notification, and slowing down under continuous use. It also offers no way for students to cancel mistaken orders.

# **Step 2: Identify three to four Sub-Problems**
Please list possible sub-problems:

1. The coin mechanism incorrectly tracks the balance and dispenses the wrong amount of change to users.

2. The vending machine lacks sensors that track the stock of the items, and it also lacks alert systems to signal when the specific items are out of stock.

3. The system runs very slow during continuous usage, which causes long lines and delay.

4. The machine lacks a transaction cancel system, which prevents users from backing out of accidental selections.


# **Step 3: Define Computational Thinking Approaches**
For each sub-problem, apply CT skills:

## **1. Faulty coin mechanism.**
CT Skill: Decomposition

**Example Solution:**

Decompose the solution into smaller sub-solutions:
1. Clear the balance so that it equals zero.
2. Scan each coin with sensors and add it to the counter.
3. If the price value is bigger than the coin value, reject the coin.
4. Subtract the price from the coin value.
5. Dispense the change properly and reset the balance to zero.

## **2. Lack of stock monitoring.**
CT Skill: Pattern Recognition

**Example Solution:**

Identify the recurring stock patterns and signals to trigger alerts:
1. Record what the sensors look like when a shelf is full vs when a shelf is completely empty to set rules for the machine to follow.
2. Keep track of every product to see how fast each item is bought and analyze which product runs out the fastest which we can use to stockpile that product.
3. Compare the sensor readings to number 1's rule to confirm that an item is out of stock instead of getting stuck in the coil.
4. When an empty pattern is recognized, immediately alert the authorities or the person in charge.

## **3. System lags**
CT Skill: Abstraction

**Example Solution**

Focusing on the essential parts like transaction queues and ignoring useless info:
1. Remove any unnecessary hardware details like the weight of the coin and focus on the necessary parts like memory usage.
2. Isolate the main causes of the delay during busy hours.
3. Clear any temporary transaction logs to free up system memory and to make the system faster.


# **Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)**
